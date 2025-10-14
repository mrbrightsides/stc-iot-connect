# STC IoT Connect - System Architecture

This document provides a comprehensive overview of the STC IoT Connect system architecture, design decisions, and technical implementation details.

## 📋 Table of Contents

1. [Overview](#overview)
2. [System Architecture](#system-architecture)
3. [Technology Stack](#technology-stack)
4. [Component Architecture](#component-architecture)
5. [Data Flow](#data-flow)
6. [API Architecture](#api-architecture)
7. [Blockchain Integration](#blockchain-integration)
8. [Security Architecture](#security-architecture)
9. [Scalability Considerations](#scalability-considerations)
10. [Design Decisions](#design-decisions)

---

## Overview

STC IoT Connect is an enterprise-grade API gateway and SDK suite that bridges IoT devices with blockchain smart contracts in the tourism and hospitality industry. The system enables secure, scalable interaction between physical infrastructure (QR scanners, smart locks, kiosks) and a decentralized blockchain network.

### Core Objectives

- **Seamless Integration**: Connect physical devices to blockchain without complexity
- **Real-Time Operations**: Process device events and blockchain transactions instantly
- **Scalability**: Handle thousands of devices across multiple locations
- **Security**: Enterprise-grade authentication and data protection
- **Reliability**: 99.9% uptime with fault tolerance

---

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         Frontend Layer                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Dashboard   │  │  Analytics   │  │  Device Mgr  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      API Gateway Layer                       │
│  ┌──────────────────────────────────────────────────┐       │
│  │  Next.js API Routes (21 endpoints)              │       │
│  │  - Authentication  - Device Mgmt  - Webhooks    │       │
│  │  - Blockchain      - Analytics    - Commands    │       │
│  └──────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────┘
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
┌─────────────────┐ ┌──────────────┐ ┌──────────────┐
│   Supabase DB   │ │  Blockchain  │ │  External    │
│   PostgreSQL    │ │   (Sepolia)  │ │   Services   │
└─────────────────┘ └──────────────┘ └──────────────┘
              ▲             ▲             ▲
              │             │             │
┌─────────────┴─────────────┴─────────────┴──────────┐
│                  IoT Device Layer                    │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │ QR Code  │  │  Smart   │  │  Kiosks  │          │
│  │ Scanners │  │  Locks   │  │          │          │
│  └──────────┘  └──────────┘  └──────────┘          │
└─────────────────────────────────────────────────────┘
```

### Layer Breakdown

#### 1. Frontend Layer (Presentation)
- **Next.js 14** with App Router
- **React 18** with Server Components
- **Tailwind CSS** for styling
- **shadcn/ui** component library
- Real-time updates via polling

#### 2. API Gateway Layer (Business Logic)
- **Next.js API Routes** for RESTful endpoints
- Request validation and sanitization
- Rate limiting and throttling
- Authentication and authorization
- Error handling and logging

#### 3. Data Layer (Persistence)
- **Supabase (PostgreSQL)** for relational data
- Real-time subscriptions for live updates
- Row-level security policies
- Connection pooling

#### 4. Blockchain Layer (Decentralization)
- **Ethereum Sepolia** testnet
- **Viem/Wagmi** for blockchain interaction
- Smart contract integration
- Transaction management

#### 5. Device Layer (Physical Integration)
- IoT devices (QR, RFID, locks)
- SDK libraries (Node.js, Python)
- RESTful API communication
- Webhook event notifications

---

## Technology Stack

### Frontend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| Next.js | 14.x | React framework with SSR/SSG |
| React | 18.x | UI library |
| TypeScript | 5.x | Type-safe JavaScript |
| Tailwind CSS | 3.x | Utility-first CSS |
| shadcn/ui | Latest | Component library |
| Lucide React | Latest | Icon library |

### Backend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| Next.js API Routes | 14.x | RESTful API endpoints |
| Supabase | Latest | PostgreSQL database + auth |
| Viem | Latest | Ethereum interaction |
| Wagmi | Latest | React hooks for web3 |
| OnchainKit | Latest | Coinbase wallet integration |

### DevOps & Infrastructure

| Tool | Purpose |
|------|---------|
| Vercel | Deployment platform |
| GitHub Actions | CI/CD pipeline |
| Docker | Containerization |
| Nginx | Reverse proxy |

---

## Component Architecture

### Frontend Components

```
src/
├── app/
│   ├── page.tsx                 # Main dashboard (13 tabs)
│   └── api/                     # API routes
│       ├── auth/               # Authentication endpoints
│       ├── devices/            # Device management
│       ├── blockchain/         # Blockchain interaction
│       ├── webhooks/           # Webhook management
│       ├── alerts/             # Alert system
│       ├── commands/           # Remote commands
│       └── analytics/          # Analytics endpoints
│
├── components/
│   └── ui/                     # Reusable UI components
│       ├── button.tsx
│       ├── card.tsx
│       ├── input.tsx
│       ├── table.tsx
│       └── tabs.tsx
│
└── lib/
    └── utils.ts                # Utility functions
```

### Key Components

#### 1. Dashboard Tabs System
```typescript
interface TabConfig {
  id: string;
  label: string;
  content: JSX.Element;
}

// 13 main tabs:
// - Tentang App (About)
// - IoT Gateway
// - Device Manager
// - Device Groups
// - Real-Time Monitor
// - Commands
// - Alerts
// - Webhooks
// - Audit Trail
// - API Docs
// - SDK Suite
// - Blockchain
// - Analytics
```

#### 2. Device Manager
- CRUD operations for devices
- Real-time status monitoring
- Device configuration
- Event history

#### 3. Real-Time Monitor
- Live event streaming
- WebSocket-style updates
- Event filtering
- Performance metrics

#### 4. Alert System
- Custom rule creation
- Automated monitoring
- Multi-channel notifications
- Alert history tracking

---

## Data Flow

### Device Event Flow

```
IoT Device → API Gateway → Validation → Database → Webhook Trigger
                ↓                           ↓
          Blockchain Tx                Real-time UI
```

### Detailed Flow

1. **Device Sends Event**
   ```
   POST /api/devices/event
   {
     "deviceId": "QR_001",
     "eventType": "qr_scan",
     "data": { "bookingId": "BK123" }
   }
   ```

2. **API Gateway Processing**
   - Validate request
   - Authenticate device
   - Rate limit check
   - Parse event data

3. **Database Storage**
   - Insert event record
   - Update device status
   - Increment counters

4. **Blockchain Integration** (if applicable)
   - Format transaction
   - Sign with private key
   - Submit to network
   - Store transaction hash

5. **Webhook Notification**
   - Find subscribed webhooks
   - Format payload
   - Send HTTP POST
   - Log delivery status

6. **UI Update**
   - Real-time monitor displays event
   - Analytics updated
   - Device status refreshed

### Authentication Flow

```
Client → Login Request → API Gateway → Supabase Auth
                              ↓
                        JWT Token ← Return Token
                              ↓
                   Store in Local Storage
                              ↓
                 Include in Authorization Header
```

---

## API Architecture

### RESTful Design Principles

- **Resource-based URLs**: `/api/devices`, `/api/bookings`
- **HTTP methods**: GET, POST, PUT, DELETE
- **Status codes**: 200, 201, 400, 401, 404, 500
- **JSON responses**: Consistent format

### API Response Format

```typescript
// Success response
{
  success: true,
  data: { ... },
  message: "Operation successful"
}

// Error response
{
  success: false,
  error: "Error message",
  code: "ERROR_CODE"
}
```

### Rate Limiting

```typescript
// Rate limit headers
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1640000000
```

### API Versioning Strategy

- URL-based versioning: `/api/v1/devices`
- Backward compatibility maintained
- Deprecation notices 6 months in advance

---

## Blockchain Integration

### Smart Contract Architecture

```solidity
contract TourismBooking {
    // Event emitted on booking
    event BookingConfirmed(
        uint256 bookingId,
        address user,
        uint256 timestamp
    );
    
    // Confirm booking function
    function confirmBooking(
        uint256 bookingId,
        string memory metadata
    ) external;
}
```

### Transaction Flow

1. **Prepare Transaction**
   ```typescript
   const tx = await contract.write.confirmBooking([
     bookingId,
     metadata
   ]);
   ```

2. **Sign Transaction**
   - Use private key from environment
   - Generate signature

3. **Submit to Network**
   - Send to Sepolia RPC
   - Wait for confirmation

4. **Store Transaction Hash**
   - Save to database
   - Link to booking record

### Gas Optimization

- Batch transactions when possible
- Use efficient data structures
- Minimize storage operations
- Implement gas price monitoring

---

## Security Architecture

### Authentication & Authorization

```
┌──────────────┐
│   Request    │
└──────┬───────┘
       ▼
┌──────────────────┐
│ JWT Validation   │
└──────┬───────────┘
       ▼
┌──────────────────┐
│ Role-Based       │
│ Access Control   │
└──────┬───────────┘
       ▼
┌──────────────────┐
│ Resource Access  │
└──────────────────┘
```

### Security Layers

#### 1. API Security
- JWT token authentication
- Rate limiting (100 req/min)
- Request validation
- SQL injection prevention
- XSS protection

#### 2. Data Security
- Encryption at rest (Supabase)
- Encryption in transit (HTTPS)
- Row-level security
- Secure environment variables

#### 3. Blockchain Security
- Private key management
- Transaction signing
- Smart contract auditing
- Gas limit controls

#### 4. Device Security
- Device registration
- API key authentication
- Webhook signature verification
- IP whitelisting

### Webhook Security

```typescript
// Webhook signature verification
const signature = crypto
  .createHmac('sha256', webhookSecret)
  .update(JSON.stringify(payload))
  .digest('hex');

// Verify signature
if (signature !== receivedSignature) {
  throw new Error('Invalid signature');
}
```

---

## Scalability Considerations

### Horizontal Scaling

- **Stateless API design**: No server-side sessions
- **Database connection pooling**: Supabase handles automatically
- **CDN for static assets**: Vercel Edge Network
- **Load balancing**: Vercel's built-in load balancer

### Vertical Scaling

- **Database optimization**: Indexed queries
- **Caching strategy**: Redis for hot data (future)
- **Code splitting**: Next.js automatic code splitting
- **Image optimization**: Next.js Image component

### Performance Optimization

```typescript
// Database query optimization
// ✅ Good - indexed query
const devices = await supabase
  .from('devices')
  .select('*')
  .eq('hotel_id', hotelId)  // indexed column
  .limit(100);

// ❌ Bad - full table scan
const devices = await supabase
  .from('devices')
  .select('*')
  .ilike('name', '%search%');  // no index
```

### Monitoring & Observability

- **Error tracking**: Sentry integration
- **Performance monitoring**: Vercel Analytics
- **Log aggregation**: Structured logging
- **Alerting**: Email/SMS for critical issues

---

## Design Decisions

### Why Next.js?

- **Full-stack framework**: Frontend + API routes
- **SEO optimization**: Server-side rendering
- **Performance**: Automatic code splitting, image optimization
- **Developer experience**: Hot reload, TypeScript support

### Why Supabase?

- **PostgreSQL**: Reliable, scalable relational database
- **Real-time**: Built-in real-time subscriptions
- **Authentication**: JWT-based auth out of the box
- **Row-level security**: Fine-grained access control

### Why Sepolia Testnet?

- **Cost-effective**: Free test ETH for development
- **Ethereum-compatible**: Easy mainnet migration
- **Well-supported**: Good tooling and documentation

### Why RESTful over GraphQL?

- **Simplicity**: Easier for IoT devices to integrate
- **Caching**: Better HTTP caching support
- **Standardization**: Well-understood patterns

### Monorepo vs Multi-repo

**Current**: Monorepo (single Next.js project)

**Pros**:
- Easier to manage
- Shared TypeScript types
- Faster development

**Future**: May split into microservices if scaling demands it

---

## Future Architecture Considerations

### Short-term (3-6 months)

- [ ] Redis caching layer
- [ ] WebSocket for real-time updates
- [ ] Background job processing (Bull/BullMQ)
- [ ] Enhanced monitoring (Datadog/New Relic)

### Mid-term (6-12 months)

- [ ] Microservices architecture
- [ ] Kubernetes deployment
- [ ] Multi-region deployment
- [ ] Advanced analytics (ClickHouse)

### Long-term (12+ months)

- [ ] Mainnet deployment
- [ ] Multi-chain support
- [ ] AI/ML integration for predictive analytics
- [ ] Edge computing for device processing

---

## Conclusion

STC IoT Connect is built with a modern, scalable architecture that balances simplicity with enterprise-grade features. The system is designed to grow from handling hundreds of devices to thousands, with clear paths for horizontal and vertical scaling.

For specific implementation details, refer to:
- **API.md** - Complete API reference
- **README.md** - Setup and deployment guide
- **CONTRIBUTING.md** - Development guidelines

---

**Document Version**: 1.0  
**Last Updated**: 2025  
**Maintained By**: ELPEEF Team
