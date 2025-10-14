# 📡 API Reference - STC IoT Connect

Complete API documentation for all endpoints in the STC IoT Connect platform.

---

## 🔑 Authentication

All API requests (except `/api/health` and `/api/version`) require authentication via JWT token.

### Headers

```http
Authorization: Bearer stc_xxx...
Content-Type: application/json
```

---

## 🚀 API Endpoints

### Base URL

```
Production: https://your-domain.com
Development: http://localhost:3000
```

---

## 📋 Table of Contents

1. [Authentication](#authentication-endpoints)
2. [User Management](#user-management)
3. [Device Operations](#device-operations)
4. [QR Code Operations](#qr-code-operations)
5. [Booking Management](#booking-management)
6. [Blockchain Integration](#blockchain-integration)
7. [Webhooks](#webhooks)
8. [Analytics](#analytics)
9. [Utilities](#utilities)

---

## 🔐 Authentication Endpoints

### 1. Register User

Create a new user account.

```http
POST /api/auth/register
```

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "fullName": "John Doe"
}
```

**Response (201):**
```json
{
  "success": true,
  "message": "User registered successfully",
  "user": {
    "id": "uuid-here",
    "email": "user@example.com",
    "fullName": "John Doe",
    "createdAt": "2024-01-01T00:00:00.000Z"
  }
}
```

**Error Responses:**
- `400` - Invalid email or password format
- `409` - Email already exists

---

### 2. Login

Authenticate and receive JWT token.

```http
POST /api/auth/login
```

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**Response (200):**
```json
{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "user": {
    "id": "uuid-here",
    "email": "user@example.com",
    "fullName": "John Doe"
  },
  "expiresIn": "24h"
}
```

**Error Responses:**
- `400` - Missing email or password
- `401` - Invalid credentials
- `500` - Server error

---

### 3. Generate API Key

Generate long-lived API key for programmatic access.

```http
POST /api/auth/generate-key
```

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**Response (200):**
```json
{
  "success": true,
  "apiKey": "stc_1a2b3c4d5e6f7g8h9i0j",
  "expiresIn": "30d",
  "createdAt": "2024-01-01T00:00:00.000Z"
}
```

**Error Responses:**
- `401` - Invalid credentials
- `500` - Server error

---

### 4. Validate Token

Validate JWT token or API key.

```http
POST /api/auth/validate
```

**Request Headers:**
```http
Authorization: Bearer stc_xxx...
```

**Response (200):**
```json
{
  "valid": true,
  "userId": "uuid-here",
  "email": "user@example.com",
  "expiresAt": "2024-01-02T00:00:00.000Z"
}
```

**Error Responses:**
- `401` - Invalid or expired token
- `500` - Server error

---

## 👤 User Management

### 1. Get User Details

Retrieve user information by ID.

```http
GET /api/user/{id}
```

**Path Parameters:**
- `id` (string, required) - User UUID

**Response (200):**
```json
{
  "success": true,
  "user": {
    "id": "uuid-here",
    "email": "user@example.com",
    "fullName": "John Doe",
    "createdAt": "2024-01-01T00:00:00.000Z",
    "bookings": [
      {
        "id": "booking-uuid",
        "reference": "BK123456",
        "hotelId": "HTL-001",
        "status": "confirmed"
      }
    ]
  }
}
```

**Error Responses:**
- `401` - Unauthorized
- `404` - User not found
- `500` - Server error

---

## 🔌 Device Operations

### 1. Register Device Event

Log a device event (registration, status change, etc).

```http
POST /api/device/event
```

**Request Headers:**
```http
Authorization: Bearer stc_xxx...
Content-Type: application/json
```

**Request Body:**
```json
{
  "deviceId": "qr-scanner-001",
  "type": "qr_scanner",
  "eventType": "device_registered",
  "userId": "user-001",
  "metadata": {
    "location": "Hotel Lobby",
    "firmware": "v2.1.0",
    "ipAddress": "192.168.1.100"
  }
}
```

**Response (201):**
```json
{
  "success": true,
  "event": {
    "id": "event-uuid",
    "deviceId": "qr-scanner-001",
    "type": "qr_scanner",
    "eventType": "device_registered",
    "timestamp": "2024-01-01T00:00:00.000Z",
    "status": "success"
  }
}
```

**Event Types:**
- `device_registered` - New device registered
- `device_online` - Device came online
- `device_offline` - Device went offline
- `qr_scan` - QR code scanned
- `door_access` - Door lock accessed
- `sensor_reading` - Sensor data received
- `error` - Device error occurred

**Error Responses:**
- `400` - Invalid request body
- `401` - Unauthorized
- `500` - Server error

---

### 2. Get Device Events

Retrieve device event history.

```http
GET /api/device/event?deviceId={deviceId}&limit={limit}&offset={offset}
```

**Query Parameters:**
- `deviceId` (string, optional) - Filter by device ID
- `eventType` (string, optional) - Filter by event type
- `limit` (number, optional) - Max results (default: 50, max: 500)
- `offset` (number, optional) - Pagination offset (default: 0)
- `startDate` (string, optional) - ISO date string
- `endDate` (string, optional) - ISO date string

**Response (200):**
```json
{
  "success": true,
  "events": [
    {
      "id": "event-uuid",
      "deviceId": "qr-scanner-001",
      "eventType": "qr_scan",
      "eventData": {
        "bookingId": "BK123456",
        "userId": "user-001"
      },
      "timestamp": "2024-01-01T12:00:00.000Z",
      "status": "success"
    }
  ],
  "pagination": {
    "total": 150,
    "limit": 50,
    "offset": 0,
    "hasMore": true
  }
}
```

**Error Responses:**
- `401` - Unauthorized
- `500` - Server error

---

## 📱 QR Code Operations

### 1. Generate QR Code

Generate QR code for booking or access.

```http
POST /api/device/qr-scan
```

**Request Headers:**
```http
Authorization: Bearer stc_xxx...
Content-Type: application/json
```

**Request Body:**
```json
{
  "action": "generate",
  "data": {
    "bookingId": "BK123456",
    "userId": "user-001",
    "roomNumber": "305",
    "expiresIn": 86400,
    "accessLevel": "guest"
  }
}
```

**Response (200):**
```json
{
  "success": true,
  "qrCode": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUg...",
  "data": {
    "bookingId": "BK123456",
    "userId": "user-001",
    "expiresAt": "2024-01-02T00:00:00.000Z"
  },
  "rawData": "encrypted-qr-payload"
}
```

**Error Responses:**
- `400` - Invalid request body
- `401` - Unauthorized
- `500` - Server error

---

### 2. Scan QR Code

Validate and decode QR code.

```http
POST /api/device/qr-scan
```

**Request Body:**
```json
{
  "action": "scan",
  "qrData": "encrypted-qr-payload",
  "deviceId": "qr-scanner-001"
}
```

**Response (200):**
```json
{
  "success": true,
  "valid": true,
  "data": {
    "bookingId": "BK123456",
    "userId": "user-001",
    "roomNumber": "305",
    "accessLevel": "guest"
  },
  "booking": {
    "reference": "BK123456",
    "hotelId": "HTL-001",
    "status": "confirmed"
  },
  "message": "Access granted"
}
```

**Error Responses:**
- `400` - Invalid or expired QR code
- `401` - Unauthorized
- `404` - Booking not found
- `500` - Server error

---

## 🏨 Booking Management

### 1. Create Booking

Create a new hotel booking.

```http
POST /api/booking
```

**Request Headers:**
```http
Authorization: Bearer stc_xxx...
Content-Type: application/json
```

**Request Body:**
```json
{
  "userId": "user-001",
  "hotelId": "HTL-001",
  "roomNumber": "305",
  "checkInDate": "2024-06-01T14:00:00.000Z",
  "checkOutDate": "2024-06-05T11:00:00.000Z",
  "guestCount": 2,
  "specialRequests": "Late check-in"
}
```

**Response (201):**
```json
{
  "success": true,
  "booking": {
    "id": "booking-uuid",
    "reference": "BK123456",
    "userId": "user-001",
    "hotelId": "HTL-001",
    "roomNumber": "305",
    "checkInDate": "2024-06-01T14:00:00.000Z",
    "checkOutDate": "2024-06-05T11:00:00.000Z",
    "status": "confirmed",
    "qrCode": "data:image/png;base64,...",
    "createdAt": "2024-01-01T00:00:00.000Z"
  },
  "blockchainTx": {
    "hash": "0x123abc...",
    "status": "pending"
  }
}
```

**Error Responses:**
- `400` - Invalid booking details
- `401` - Unauthorized
- `409` - Room not available
- `500` - Server error

---

### 2. Verify Booking

Verify user's booking details.

```http
GET /api/booking/verify/{user_id}
```

**Path Parameters:**
- `user_id` (string, required) - User ID

**Query Parameters:**
- `bookingReference` (string, optional) - Specific booking reference

**Response (200):**
```json
{
  "success": true,
  "bookings": [
    {
      "id": "booking-uuid",
      "reference": "BK123456",
      "hotelId": "HTL-001",
      "roomNumber": "305",
      "checkInDate": "2024-06-01T14:00:00.000Z",
      "checkOutDate": "2024-06-05T11:00:00.000Z",
      "status": "confirmed",
      "qrCode": "data:image/png;base64,..."
    }
  ]
}
```

**Booking Statuses:**
- `pending` - Awaiting confirmation
- `confirmed` - Booking confirmed
- `checked_in` - Guest checked in
- `checked_out` - Guest checked out
- `cancelled` - Booking cancelled

**Error Responses:**
- `401` - Unauthorized
- `404` - No bookings found
- `500` - Server error

---

## ⛓️ Blockchain Integration

### 1. Call Smart Contract

Execute smart contract function.

```http
POST /api/contract/call
```

**Request Headers:**
```http
Authorization: Bearer stc_xxx...
Content-Type: application/json
```

**Request Body:**
```json
{
  "functionName": "logCheckIn",
  "args": ["user-001", "HTL-001", "305", "1704067200"],
  "value": "0"
}
```

**Response (200):**
```json
{
  "success": true,
  "transaction": {
    "hash": "0x123abc456def...",
    "from": "0xYourAddress...",
    "to": "0xContractAddress...",
    "status": "pending",
    "blockNumber": null,
    "gasUsed": null
  },
  "receipt": null
}
```

**Available Functions:**
- `logCheckIn(userId, hotelId, roomNumber, timestamp)`
- `logCheckOut(userId, hotelId, roomNumber, timestamp)`
- `logDeviceEvent(deviceId, eventType, timestamp, metadata)`
- `verifyBooking(bookingId)` - Returns boolean

**Error Responses:**
- `400` - Invalid function or arguments
- `401` - Unauthorized
- `500` - Blockchain error

---

### 2. Get Transaction Status

Get blockchain transaction details.

```http
GET /api/transaction/{hash}
```

**Path Parameters:**
- `hash` (string, required) - Transaction hash (0x...)

**Response (200):**
```json
{
  "success": true,
  "transaction": {
    "hash": "0x123abc456def...",
    "blockNumber": 12345678,
    "status": "confirmed",
    "from": "0xFromAddress...",
    "to": "0xToAddress...",
    "gasUsed": "21000",
    "effectiveGasPrice": "30000000000",
    "timestamp": "2024-01-01T00:00:00.000Z",
    "confirmations": 15
  }
}
```

**Transaction Statuses:**
- `pending` - Transaction submitted, awaiting mining
- `confirmed` - Transaction mined and confirmed
- `failed` - Transaction failed
- `not_found` - Transaction hash not found

**Error Responses:**
- `401` - Unauthorized
- `404` - Transaction not found
- `500` - Server error

---

## 🪝 Webhooks

### 1. Register Webhook

Subscribe to device events via webhook.

```http
POST /api/webhooks/register
```

**Request Headers:**
```http
Authorization: Bearer stc_xxx...
Content-Type: application/json
```

**Request Body:**
```json
{
  "name": "Hotel Main Webhook",
  "url": "https://your-server.com/webhook-endpoint",
  "events": [
    "qr_scan",
    "door_access",
    "device_online",
    "device_offline",
    "sensor_reading"
  ],
  "active": true,
  "retryConfig": {
    "maxRetries": 3,
    "retryDelay": 5000
  }
}
```

**Response (201):**
```json
{
  "success": true,
  "webhook": {
    "id": "webhook-uuid",
    "name": "Hotel Main Webhook",
    "url": "https://your-server.com/webhook-endpoint",
    "events": ["qr_scan", "door_access"],
    "secret": "whsec_abc123...",
    "active": true,
    "createdAt": "2024-01-01T00:00:00.000Z"
  }
}
```

**Webhook Signature:**
All webhooks include a signature header for verification:
```http
X-Webhook-Signature: sha256=abc123...
X-Webhook-Timestamp: 1704067200
```

**Verify Signature (Node.js):**
```javascript
const crypto = require('crypto');

function verifyWebhook(payload, signature, secret) {
  const hmac = crypto.createHmac('sha256', secret);
  const digest = 'sha256=' + hmac.update(payload).digest('hex');
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(digest)
  );
}
```

**Error Responses:**
- `400` - Invalid webhook configuration
- `401` - Unauthorized
- `500` - Server error

---

### 2. Trigger Webhook

Manually trigger webhook for testing.

```http
POST /api/webhooks/trigger
```

**Request Body:**
```json
{
  "webhookId": "webhook-uuid",
  "testEvent": {
    "eventType": "qr_scan",
    "deviceId": "qr-scanner-001",
    "timestamp": "2024-01-01T00:00:00.000Z",
    "data": {
      "bookingId": "BK123456",
      "userId": "user-001"
    }
  }
}
```

**Response (200):**
```json
{
  "success": true,
  "delivery": {
    "webhookId": "webhook-uuid",
    "status": "delivered",
    "statusCode": 200,
    "responseTime": 145,
    "attempts": 1
  }
}
```

**Error Responses:**
- `400` - Invalid webhook or event
- `401` - Unauthorized
- `404` - Webhook not found
- `500` - Server error

---

## 📊 Analytics

### 1. Get Real-Time Analytics

Get live platform metrics.

```http
GET /api/analytics/realtime
```

**Request Headers:**
```http
Authorization: Bearer stc_xxx...
```

**Query Parameters:**
- `deviceId` (string, optional) - Filter by specific device
- `hotelId` (string, optional) - Filter by hotel
- `timeWindow` (number, optional) - Time window in seconds (default: 3600)

**Response (200):**
```json
{
  "success": true,
  "analytics": {
    "timestamp": "2024-01-01T12:00:00.000Z",
    "activeDevices": 45,
    "totalEvents": 1234,
    "eventsPerMinute": 12.5,
    "averageLatency": 120,
    "successRate": 99.5,
    "deviceBreakdown": {
      "qr_scanner": 20,
      "smart_lock": 15,
      "kiosk": 10
    },
    "eventBreakdown": {
      "qr_scan": 500,
      "door_access": 400,
      "device_online": 150,
      "sensor_reading": 184
    },
    "topDevices": [
      {
        "deviceId": "qr-scanner-001",
        "eventCount": 89,
        "avgLatency": 95
      }
    ]
  }
}
```

**Error Responses:**
- `401` - Unauthorized
- `500` - Server error

---

## 🛠️ Utilities

### 1. Health Check

Check API health status.

```http
GET /api/health
```

**No authentication required**

**Response (200):**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00.000Z",
  "uptime": 86400,
  "version": "1.0.0",
  "services": {
    "database": "connected",
    "blockchain": "connected",
    "cache": "connected"
  }
}
```

---

### 2. Get API Version

Get current API version information.

```http
GET /api/version
```

**No authentication required**

**Response (200):**
```json
{
  "version": "1.0.0",
  "apiVersion": "v1",
  "releaseDate": "2024-01-01",
  "environment": "production",
  "features": [
    "device-management",
    "blockchain-integration",
    "real-time-analytics",
    "webhooks",
    "smart-alerts"
  ]
}
```

---

## 🔐 Rate Limiting

All API endpoints are rate limited:

**Headers:**
```http
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1704067200
```

**Limits:**
- **Free Tier**: 100 requests/minute
- **Pro Tier**: 1000 requests/minute
- **Enterprise**: Custom limits

**Rate Limit Exceeded (429):**
```json
{
  "error": "Rate limit exceeded",
  "message": "Too many requests. Please try again in 60 seconds.",
  "retryAfter": 60
}
```

---

## 🌐 Webhook Event Payloads

### Device Event Webhook

```json
{
  "eventId": "event-uuid",
  "eventType": "qr_scan",
  "timestamp": "2024-01-01T12:00:00.000Z",
  "device": {
    "id": "qr-scanner-001",
    "type": "qr_scanner",
    "location": "Hotel Lobby"
  },
  "data": {
    "bookingId": "BK123456",
    "userId": "user-001",
    "accessGranted": true
  },
  "user": {
    "id": "user-001",
    "email": "guest@example.com",
    "fullName": "John Doe"
  }
}
```

### Booking Event Webhook

```json
{
  "eventId": "event-uuid",
  "eventType": "booking_confirmed",
  "timestamp": "2024-01-01T12:00:00.000Z",
  "booking": {
    "id": "booking-uuid",
    "reference": "BK123456",
    "hotelId": "HTL-001",
    "roomNumber": "305",
    "status": "confirmed"
  },
  "blockchainTx": {
    "hash": "0x123abc...",
    "status": "confirmed"
  }
}
```

---

## 📝 Error Responses

Standard error format:

```json
{
  "error": "Error type",
  "message": "Human-readable error message",
  "code": "ERROR_CODE",
  "details": {
    "field": "Specific field error"
  },
  "timestamp": "2024-01-01T12:00:00.000Z",
  "requestId": "req-uuid"
}
```

**Common Error Codes:**
- `INVALID_REQUEST` - Malformed request
- `UNAUTHORIZED` - Missing or invalid authentication
- `FORBIDDEN` - Insufficient permissions
- `NOT_FOUND` - Resource not found
- `CONFLICT` - Resource conflict
- `RATE_LIMITED` - Too many requests
- `SERVER_ERROR` - Internal server error
- `BLOCKCHAIN_ERROR` - Blockchain operation failed
- `DATABASE_ERROR` - Database operation failed

---

## 🧪 Testing with Postman

Import collection:

```json
{
  "info": {
    "name": "STC IoT Connect API",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "auth": {
    "type": "bearer",
    "bearer": [
      {
        "key": "token",
        "value": "{{api_key}}",
        "type": "string"
      }
    ]
  },
  "variable": [
    {
      "key": "base_url",
      "value": "https://your-domain.com"
    },
    {
      "key": "api_key",
      "value": "stc_xxx..."
    }
  ]
}
```

---

**Complete API documentation. Ready to integrate! 🚀**
