# 🚀 Supabase Setup for STC IoT Connect - Phase 1

## Prerequisites
- Supabase account (free tier works great!)
- Project created in Supabase dashboard

## Step 1: Create Supabase Project
1. Go to [supabase.com](https://supabase.com)
2. Create a new project
3. Note down your **Project URL** and **Anon Key**

## Step 2: Set Environment Variables
Create a `.env.local` file in project root:

```bash
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=your-anon-key-here
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production
```

## Step 3: Run SQL Schema
Go to Supabase SQL Editor and run this schema:

```sql
-- Users table
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email TEXT UNIQUE NOT NULL,
  password_hash TEXT NOT NULL,
  name TEXT NOT NULL,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- API Keys table
CREATE TABLE api_keys (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  name TEXT NOT NULL,
  key TEXT UNIQUE NOT NULL,
  permissions TEXT[] NOT NULL DEFAULT '{"read", "write"}',
  is_active BOOLEAN DEFAULT TRUE,
  last_used TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Bookings table
CREATE TABLE bookings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  booking_id TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  date TEXT NOT NULL,
  hotel TEXT NOT NULL,
  room_number TEXT,
  tx_hash TEXT NOT NULL,
  verified BOOLEAN DEFAULT FALSE,
  verified_at TIMESTAMP WITH TIME ZONE,
  qr_code TEXT,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Devices table
CREATE TABLE devices (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  device_id TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  type TEXT NOT NULL,
  location TEXT,
  status TEXT DEFAULT 'offline' CHECK (status IN ('online', 'offline', 'error')),
  is_active BOOLEAN DEFAULT TRUE,
  last_seen TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Device Events table
CREATE TABLE device_events (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  device_id TEXT REFERENCES devices(device_id) ON DELETE CASCADE,
  event_type TEXT NOT NULL,
  booking_id TEXT,
  metadata JSONB,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Indexes for better performance
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_api_keys_user_id ON api_keys(user_id);
CREATE INDEX idx_api_keys_key ON api_keys(key);
CREATE INDEX idx_bookings_user_id ON bookings(user_id);
CREATE INDEX idx_bookings_booking_id ON bookings(booking_id);
CREATE INDEX idx_devices_device_id ON devices(device_id);
CREATE INDEX idx_device_events_device_id ON device_events(device_id);
CREATE INDEX idx_device_events_booking_id ON device_events(booking_id);

-- RLS Policies (Row Level Security)
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE api_keys ENABLE ROW LEVEL SECURITY;
ALTER TABLE bookings ENABLE ROW LEVEL SECURITY;
ALTER TABLE devices ENABLE ROW LEVEL SECURITY;
ALTER TABLE device_events ENABLE ROW LEVEL SECURITY;

-- Users can only see their own data
CREATE POLICY "Users can view own data" ON users
  FOR SELECT USING (auth.uid() = id::text);

CREATE POLICY "Users can update own data" ON users
  FOR UPDATE USING (auth.uid() = id::text);

-- API Keys policies
CREATE POLICY "Users can view own API keys" ON api_keys
  FOR ALL USING (auth.uid() = user_id::text);

-- Bookings policies
CREATE POLICY "Users can view own bookings" ON bookings
  FOR ALL USING (auth.uid() = user_id::text);

-- Devices can be viewed by all authenticated users
CREATE POLICY "Authenticated users can view devices" ON devices
  FOR SELECT USING (auth.role() = 'authenticated');

-- Device events can be viewed by all authenticated users
CREATE POLICY "Authenticated users can view device events" ON device_events
  FOR SELECT USING (auth.role() = 'authenticated');
```

## Step 4: Test the Setup

### Register a new user:
```bash
curl -X POST http://localhost:3000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123",
    "name": "Test User"
  }'
```

### Login:
```bash
curl -X POST http://localhost:3000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }'
```

### Generate API Key:
```bash
curl -X POST http://localhost:3000/api/auth/generate-key \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{
    "name": "Production Key",
    "permissions": ["read", "write"]
  }'
```

## Step 5: Blockchain Integration (Optional)

For real blockchain transactions, you'll need a wallet with:
1. Private key (store securely in environment variables)
2. Sepolia ETH for gas fees (get from faucet)

Add to `.env.local`:
```bash
WALLET_PRIVATE_KEY=0xyour-private-key-here
```

## 🎉 You're All Set!

Phase 1 is now complete with:
- ✅ Real authentication system
- ✅ Database persistence
- ✅ API key management
- ✅ Booking system with blockchain
- ✅ QR code generation

## Next Steps (Phase 2+)
- WebSocket for real-time updates
- MQTT broker integration
- Multiple device types
- Advanced analytics
- Mobile app

---

**Security Notes:**
- Never commit `.env.local` to git
- Use strong JWT_SECRET in production
- Enable Supabase backup
- Monitor API usage
- Rotate API keys regularly
