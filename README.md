# STC Connect 🌀

**Enterprise-Grade IoT Gateway & Blockchain Integration Platform for Tourism Industry**

**Part of the STC Ecosystem** 🌟

STC IoT Connect is a comprehensive API gateway and SDK suite that bridges physical IoT devices with blockchain smart contracts, enabling secure, scalable interactions for modern tourism infrastructure. As a critical component of the **Human Cyber-Physical Systems (HCPS) Tourism 5.0 Framework**, it serves as the infrastructure layer connecting physical devices, cyber systems, human interfaces, and governance mechanisms. From QR scanners and smart locks to kiosks and RFID readers, this platform powers the next generation of connected hospitality.

[![SWH](https://img.shields.io/badge/archived%20at-Software%20Heritage-orange)](https://archive.softwareheritage.org/browse/directory/824f9ed66775c2764adb15796448bc4994e3982b/?origin_url=https://doi.org/10.5281/zenodo.17216998&path=mrbrightsides-stc-iot-connect-39c932e&release=2&snapshot=f6bdb64ab13314f50b0a3b3211d1c9fdeeddc280)
[![OpenAIRE](https://img.shields.io/badge/indexed%20by-OpenAIRE-blue)](https://explore.openaire.eu/search/result?pid=10.5281%2Fzenodo.17217000)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17217000.svg)](https://doi.org/10.5281/zenodo.17217000)
[![Built with Next.js](https://img.shields.io/badge/Built%20with-Next.js%2015-000000?style=flat&logo=next.js)](https://nextjs.org/)
[![Powered by Base](https://img.shields.io/badge/Powered%20by-Base-0052FF?style=flat&logo=coinbase)](https://base.org/)
[![Supabase](https://img.shields.io/badge/Database-Supabase-3ECF8E?style=flat&logo=supabase)](https://supabase.com/)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.8-3178C6?style=flat&logo=typescript)](https://www.typescriptlang.org/)

---

## 📂 Endpoints
| Method | Endpoint                 | Deskripsi                       |
| ------ | ------------------------ | ------------------------------- |
| POST   | `/auth/login`            | Login user, generate token JWT  |
| POST   | `/booking/create`        | Buat booking baru               |
| GET    | `/booking/verify`        | Verifikasi status booking       |
| POST   | `/device/log`            | Simpan event IoT device         |
| GET    | `/transaction/{tx_hash}` | Cek detail transaksi blockchain |
| GET    | `/analytics/realtime`    | Ambil data realtime analytics   |
| POST   | `/contract/call`         | Panggil fungsi smart contract   |

---

## 🌟 Features

### 🔌 IoT Device Management
- **Multi-Protocol Support**: QR scanners, RFID readers, smart locks, kiosks
- **Real-Time Monitoring**: Live device health tracking with 2-second updates
- **Remote Commands**: Control devices from anywhere with instant execution
- **Device Grouping**: Organize by hotel, floor, department, or custom categories
- **Bulk Operations**: Manage multiple devices simultaneously

### 🔗 Blockchain Integration
- **Smart Contract Interaction**: Direct integration with Sepolia testnet
- **OnchainKit Integration**: Seamless wallet and transaction management
- **Transaction Tracking**: Monitor all blockchain operations in real-time
- **Event Logging**: Complete on-chain audit trail

### 📊 Advanced Analytics
- **Real-Time Dashboards**: Live metrics and performance monitoring
- **Device Performance**: Track uptime, latency, success rates
- **Event Streaming**: WebSocket-powered live event feeds
- **Custom Reports**: Export data for business intelligence

### ⚡ Smart Alerts & Automation
- **Rules Engine**: Create custom alert conditions
- **Multi-Channel Notifications**: Webhooks, Email, SMS, Logs
- **Automated Responses**: Trigger actions based on device events
- **Alert History**: Complete tracking with resolution status

### 🪝 Webhook Management
- **Event Subscriptions**: Subscribe to specific device events
- **Secure Delivery**: Signature verification for webhooks
- **Retry Logic**: Automatic retry for failed deliveries
- **Activity Logs**: Track webhook success/failure rates

### 🔐 Security & Compliance
- **JWT Authentication**: Secure API key management
- **Complete Audit Trail**: Track every action with IP logging
- **Role-Based Access**: Fine-grained permission control
- **Compliance Ready**: Export audit logs for regulations

### 📡 RESTful API
- **21 API Endpoints**: Comprehensive REST API coverage
- **OpenAPI Specification**: Complete API documentation
- **Rate Limiting**: Built-in rate limit headers
- **SDK Libraries**: Node.js and Python client libraries

---

## 🛠️ Tech Stack

### Frontend
- **Framework**: Next.js 15.3.4 (App Router)
- **UI Library**: React 19.1.0
- **Styling**: Tailwind CSS 3.4
- **Components**: Radix UI + shadcn/ui
- **State Management**: React Hooks
- **Charts**: Recharts
- **Animations**: Framer Motion

### Backend & Infrastructure
- **Runtime**: Node.js
- **Database**: Supabase (PostgreSQL)
- **Authentication**: JWT + bcrypt
- **Blockchain**: 
  - Viem 2.30.6
  - Wagmi 2.15.5
  - OnchainKit 0.38.17
- **Network**: Sepolia Testnet (Infura RPC)

### DevOps & Tools
- **Language**: TypeScript 5.8
- **Package Manager**: npm/yarn/pnpm
- **Logging**: Winston
- **QR Codes**: qrcode library
- **Deployment**: Vercel-ready

---

## 📦 Installation

### Prerequisites
- Node.js 18+ or Bun
- npm, yarn, or pnpm
- Supabase account
- Infura API key (for Sepolia)
- Wallet for blockchain interaction

### Quick Start

```bash
# Clone the repository
git clone <your-repo-url>
cd stc-iot-connect

# Install dependencies
npm install
# or
yarn install
# or
pnpm install

# Run development server
npm run dev
# or
yarn dev
# or
pnpm dev

# Open http://localhost:3000
```

### Build for Production

```bash
# Build the application
npm run build

# Start production server
npm start
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env.local` file in the root directory:

```env
# Supabase Configuration
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key

# Blockchain Configuration
NEXT_PUBLIC_INFURA_PROJECT_ID=your_infura_project_id
NEXT_PUBLIC_CONTRACT_ADDRESS=your_contract_address

# JWT Secret (for authentication)
JWT_SECRET=your_secret_key_here

# API Configuration
NEXT_PUBLIC_API_BASE_URL=http://localhost:3000
```

### Supabase Database Setup

Run these SQL commands in your Supabase SQL editor:

```sql
-- Create users table
CREATE TABLE users (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  full_name TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create devices table
CREATE TABLE devices (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  device_id TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  type TEXT NOT NULL,
  status TEXT DEFAULT 'offline',
  location TEXT,
  hotel_id TEXT,
  metadata JSONB,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create bookings table
CREATE TABLE bookings (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  booking_reference TEXT UNIQUE NOT NULL,
  hotel_id TEXT NOT NULL,
  room_number TEXT,
  check_in_date TIMESTAMP WITH TIME ZONE,
  check_out_date TIMESTAMP WITH TIME ZONE,
  status TEXT DEFAULT 'pending',
  qr_code TEXT,
  blockchain_tx_hash TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create device_events table
CREATE TABLE device_events (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  device_id TEXT NOT NULL,
  event_type TEXT NOT NULL,
  event_data JSONB,
  user_id TEXT,
  timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  status TEXT DEFAULT 'success'
);

-- Create webhooks table
CREATE TABLE webhooks (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  name TEXT NOT NULL,
  url TEXT NOT NULL,
  events TEXT[] NOT NULL,
  secret TEXT NOT NULL,
  active BOOLEAN DEFAULT true,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create audit_logs table
CREATE TABLE audit_logs (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  user_id TEXT,
  action TEXT NOT NULL,
  category TEXT NOT NULL,
  details JSONB,
  ip_address TEXT,
  status TEXT DEFAULT 'success',
  timestamp TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create indexes for better performance
CREATE INDEX idx_devices_device_id ON devices(device_id);
CREATE INDEX idx_bookings_user_id ON bookings(user_id);
CREATE INDEX idx_device_events_device_id ON device_events(device_id);
CREATE INDEX idx_device_events_timestamp ON device_events(timestamp DESC);
CREATE INDEX idx_audit_logs_timestamp ON audit_logs(timestamp DESC);
```

---

## 📚 API Documentation

### Authentication

All API requests require authentication via API key:

```bash
# Generate API Key
POST /api/auth/generate-key
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "your_password"
}

# Response
{
  "apiKey": "stc_xxx...",
  "expiresIn": "30d"
}
```

Use the API key in subsequent requests:

```bash
Authorization: Bearer stc_xxx...
```

### Core Endpoints

#### Device Management

```bash
# Register Device
POST /api/device/event
Authorization: Bearer stc_xxx...
Content-Type: application/json

{
  "deviceId": "qr-scanner-001",
  "type": "qr_scanner",
  "eventType": "device_registered",
  "metadata": {
    "location": "Hotel Lobby",
    "firmware": "v2.1.0"
  }
}

# Get Device Events
GET /api/device/event?deviceId=qr-scanner-001&limit=50
Authorization: Bearer stc_xxx...
```

#### QR Code Operations

```bash
# Generate QR Code for Booking
POST /api/device/qr-scan
Authorization: Bearer stc_xxx...
Content-Type: application/json

{
  "action": "generate",
  "data": {
    "bookingId": "BK123456",
    "userId": "user-001",
    "expiresIn": 86400
  }
}

# Scan QR Code
POST /api/device/qr-scan
Authorization: Bearer stc_xxx...
Content-Type: application/json

{
  "action": "scan",
  "qrData": "encoded_qr_data_here"
}
```

#### Booking Management

```bash
# Create Booking
POST /api/booking
Authorization: Bearer stc_xxx...
Content-Type: application/json

{
  "userId": "user-001",
  "hotelId": "HTL-001",
  "roomNumber": "305",
  "checkInDate": "2024-06-01",
  "checkOutDate": "2024-06-05"
}

# Verify Booking
GET /api/booking/verify/{user_id}
Authorization: Bearer stc_xxx...
```

#### Blockchain Integration

```bash
# Call Smart Contract
POST /api/contract/call
Authorization: Bearer stc_xxx...
Content-Type: application/json

{
  "functionName": "logCheckIn",
  "args": ["user-001", "HTL-001", "305"],
  "value": "0"
}

# Get Transaction Status
GET /api/transaction/{transaction_hash}
Authorization: Bearer stc_xxx...
```

#### Webhooks

```bash
# Register Webhook
POST /api/webhooks/register
Authorization: Bearer stc_xxx...
Content-Type: application/json

{
  "url": "https://your-server.com/webhook",
  "events": ["qr_scan", "door_access", "device_online"],
  "name": "Hotel Main Webhook"
}
```

#### Analytics

```bash
# Get Real-Time Analytics
GET /api/analytics/realtime
Authorization: Bearer stc_xxx...

# Response
{
  "activeDevices": 45,
  "totalEvents": 1234,
  "averageLatency": 120,
  "successRate": 99.5,
  "recentEvents": [...]
}
```

### Complete API Reference

For full API documentation with request/response schemas, visit the **API Docs** tab in the dashboard at `/`.

---

## 🎯 Usage Examples

### Node.js SDK Example

```javascript
const STCIoT = require('stc-iot-sdk');

// Initialize client
const client = new STCIoT({
  apiKey: 'stc_xxx...',
  baseUrl: 'https://stc-connect.elpeef.com'
});

// Register a device
await client.devices.register({
  deviceId: 'smart-lock-101',
  type: 'smart_lock',
  location: 'Room 305'
});

// Generate QR code for check-in
const qrCode = await client.qr.generate({
  bookingId: 'BK123456',
  userId: 'user-001',
  expiresIn: 86400 // 24 hours
});

// Listen for device events
client.on('device.event', (event) => {
  console.log('Device event:', event);
  
  if (event.type === 'door_access') {
    // Log to blockchain
    client.blockchain.logEvent({
      eventType: 'door_access',
      deviceId: event.deviceId,
      userId: event.userId
    });
  }
});
```

### Python SDK Example

```python
from stc_iot import STCIoTClient

# Initialize client
client = STCIoTClient(
    api_key='stc_xxx...',
    base_url='https://your-domain.com'
)

# Register a device
device = client.devices.register(
    device_id='kiosk-001',
    type='kiosk',
    location='Hotel Lobby'
)

# Generate QR code
qr_code = client.qr.generate(
    booking_id='BK123456',
    user_id='user-001',
    expires_in=86400
)

# Subscribe to webhook events
@client.webhook('/webhook-endpoint')
def handle_device_event(event):
    print(f"Received event: {event['type']}")
    
    if event['type'] == 'qr_scan':
        # Process check-in
        booking = client.bookings.verify(event['user_id'])
        print(f"Booking verified: {booking['reference']}")
```

### cURL Examples

```bash
# Health Check
curl -X GET https://your-domain.com/api/health

# Authenticate & Get API Key
curl -X POST https://your-domain.com/api/auth/generate-key \
  -H "Content-Type: application/json" \
  -d '{
    "email": "admin@hotel.com",
    "password": "SecurePass123"
  }'

# Register Device with Authentication
curl -X POST https://your-domain.com/api/device/event \
  -H "Authorization: Bearer stc_xxx..." \
  -H "Content-Type: application/json" \
  -d '{
    "deviceId": "qr-001",
    "type": "qr_scanner",
    "eventType": "device_registered",
    "metadata": {
      "location": "Lobby",
      "firmware": "v2.1.0"
    }
  }'

# Generate QR Code
curl -X POST https://your-domain.com/api/device/qr-scan \
  -H "Authorization: Bearer stc_xxx..." \
  -H "Content-Type: application/json" \
  -d '{
    "action": "generate",
    "data": {
      "bookingId": "BK123456",
      "userId": "user-001",
      "expiresIn": 86400
    }
  }'
```

---

## 🏗️ Project Structure

```
stc-iot-connect/
├── src/
│   ├── app/
│   │   ├── api/                    # API routes
│   │   │   ├── auth/              # Authentication endpoints
│   │   │   ├── booking/           # Booking management
│   │   │   ├── device/            # Device operations
│   │   │   ├── contract/          # Blockchain interactions
│   │   │   ├── webhooks/          # Webhook management
│   │   │   ├── analytics/         # Real-time analytics
│   │   │   └── transaction/       # Transaction tracking
│   │   ├── layout.tsx             # Root layout
│   │   ├── page.tsx               # Main dashboard
│   │   └── providers.tsx          # Context providers
│   ├── components/
│   │   ├── blockchain/            # Blockchain components
│   │   ├── iot/                   # IoT-specific components
│   │   │   ├── APIDocumentation.tsx
│   │   │   ├── DeviceManager.tsx
│   │   │   ├── RealTimeMonitor.tsx
│   │   │   ├── AlertsManager.tsx
│   │   │   ├── DeviceCommands.tsx
│   │   │   ├── DeviceGroups.tsx
│   │   │   ├── WebhookManager.tsx
│   │   │   └── AuditTrail.tsx
│   │   └── ui/                    # UI components (shadcn)
│   ├── lib/
│   │   ├── supabase.ts            # Supabase client
│   │   ├── web3.ts                # Web3 utilities
│   │   ├── auth.ts                # Auth helpers
│   │   ├── qrcode.ts              # QR generation
│   │   └── logger.ts              # Winston logger
│   └── types/
│       └── database.ts            # TypeScript types
├── public/
│   └── .well-known/
│       └── farcaster.json         # Farcaster integration
├── package.json
├── tsconfig.json
├── tailwind.config.js
└── README.md
```

---

## 🚀 Deployment

### Deploy to Vercel (Recommended)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-repo-url>
   git push -u origin main
   ```

2. **Connect to Vercel**
   - Visit [vercel.com](https://vercel.com)
   - Import your GitHub repository
   - Add environment variables from `.env.local`
   - Deploy!

3. **Environment Variables in Vercel**
   - Go to Project Settings → Environment Variables
   - Add all variables from your `.env.local`
   - Redeploy if needed

### Manual Deployment

```bash
# Build for production
npm run build

# Start production server
npm start

# Or use PM2 for process management
pm2 start npm --name "stc-iot" -- start
```

---

## 🔒 Security Best Practices

1. **API Keys**: Never commit API keys to version control
2. **Environment Variables**: Use `.env.local` for sensitive data
3. **JWT Secrets**: Use strong, random secrets (32+ characters)
4. **HTTPS Only**: Always use HTTPS in production
5. **Rate Limiting**: Implement rate limiting for public endpoints
6. **Input Validation**: Validate all user inputs
7. **Audit Logs**: Review audit logs regularly
8. **Webhook Signatures**: Always verify webhook signatures

---

## 📊 Dashboard Features

### 13 Comprehensive Tabs

1. **Tentang App**: Educational overview (Indonesian)
2. **IoT Gateway**: Device registration and management
3. **Device Manager**: CRUD operations for devices
4. **Device Groups**: Organize devices by categories
5. **Real-Time Monitor**: Live device event streaming
6. **Commands**: Remote device control center
7. **Alerts**: Smart alert rules and notifications
8. **Webhooks**: Webhook subscriptions and management
9. **Audit Trail**: Complete security audit logs
10. **API Docs**: OpenAPI specification browser
11. **SDK Suite**: Node.js and Python code examples
12. **Blockchain**: Smart contract integration
13. **Analytics**: Real-time performance metrics

---

## 🛠️ Development

### Run Development Server

```bash
npm run dev
```

### Type Checking

```bash
npx tsc --noEmit
```

### Linting

```bash
npm run lint
```

### Database Migrations

When adding new Supabase tables:

1. Update SQL schema in Supabase dashboard
2. Update TypeScript types in `src/types/database.ts`
3. Test with development data

---

## 🤝 Contributing

We welcome contributions! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow TypeScript best practices
- Write meaningful commit messages
- Add comments for complex logic
- Update documentation for new features
- Test thoroughly before submitting PR

---

## 🐛 Troubleshooting

### Common Issues

**Build Errors**
```bash
# Clear cache and reinstall
rm -rf .next node_modules
npm install
npm run build
```

**Supabase Connection Issues**
- Verify `NEXT_PUBLIC_SUPABASE_URL` and `NEXT_PUBLIC_SUPABASE_ANON_KEY`
- Check Supabase project status
- Verify network connectivity

**Blockchain Connection Issues**
- Verify Infura project ID
- Check Sepolia network status
- Ensure contract address is correct
- Verify wallet has test ETH

**Authentication Errors**
- Verify JWT_SECRET is set
- Check API key format (must start with `stc_`)
- Ensure token hasn't expired

---

## 📝 License

This project is proprietary software. All rights reserved.

---

## 📧 Support

For support and inquiries:

- **Email**: support@elpeef.com
- **Issues**: [GitHub Issues](https://github.com/mrbrightsides/stc-iot-connect/issues)

---

## 🙏 Acknowledgments

Built with:
- [Next.js](https://nextjs.org/) - The React Framework
- [Supabase](https://supabase.com/) - Open Source Firebase Alternative
- [OnchainKit](https://onchainkit.xyz/) - Coinbase's Web3 Toolkit
- [Viem](https://viem.sh/) - TypeScript Interface for Ethereum
- [shadcn/ui](https://ui.shadcn.com/) - Beautiful UI Components
- [Tailwind CSS](https://tailwindcss.com/) - Utility-First CSS
- [Base](https://base.org/) - Ethereum L2 Network

---

**Built with ❤️ for the Future of Tourism Technology**

🌐 Bridging Physical Infrastructure with Blockchain Innovation
