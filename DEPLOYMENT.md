# 🚀 Deployment Guide - STC IoT Connect

Complete guide for deploying STC IoT Connect to production environments.

---

## 📋 Pre-Deployment Checklist

### Required Services

- [ ] **Vercel Account** - For hosting (recommended)
- [ ] **Supabase Project** - For database
- [ ] **Infura Account** - For blockchain RPC
- [ ] **Domain Name** - Optional, for custom domain
- [ ] **SSL Certificate** - Auto-provided by Vercel

### Environment Configuration

- [ ] All environment variables documented
- [ ] Database schema created in Supabase
- [ ] Smart contract deployed to Sepolia
- [ ] API keys generated and tested
- [ ] JWT secret generated (32+ characters)

---

## 🌐 Deploy to Vercel (Recommended)

### Step 1: Prepare Repository

```bash
# Initialize git if not already done
git init

# Add all files
git add .

# Commit
git commit -m "Initial deployment"

# Create repository on GitHub/GitLab/Bitbucket
# Then push
git remote add origin <your-repo-url>
git push -u origin main
```

### Step 2: Connect to Vercel

1. Visit [vercel.com](https://vercel.com)
2. Click "Add New..." → "Project"
3. Import your Git repository
4. Select the repository: `stc-iot-connect`

### Step 3: Configure Build Settings

Vercel will auto-detect Next.js. Confirm these settings:

```
Framework Preset: Next.js
Build Command: npm run build
Output Directory: .next
Install Command: npm install
Development Command: npm run dev
```

### Step 4: Add Environment Variables

In the Vercel dashboard, go to **Settings** → **Environment Variables**:

```env
# Supabase
NEXT_PUBLIC_SUPABASE_URL=https://xxx.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJxxx...

# Blockchain
NEXT_PUBLIC_INFURA_PROJECT_ID=your_infura_id
NEXT_PUBLIC_CONTRACT_ADDRESS=0x...

# Authentication
JWT_SECRET=your_32_character_secret_here

# API
NEXT_PUBLIC_API_BASE_URL=https://your-domain.vercel.app
```

**Important**: 
- Set all variables for **Production**, **Preview**, and **Development** environments
- Use different Supabase projects for production and development
- Use different JWT secrets for each environment

### Step 5: Deploy

1. Click **Deploy**
2. Wait 2-3 minutes for build completion
3. Visit your deployment URL
4. Test all features

### Step 6: Custom Domain (Optional)

1. Go to **Settings** → **Domains**
2. Add your custom domain
3. Configure DNS records as instructed
4. Wait for SSL certificate provisioning (automatic)

---

## 🐳 Deploy with Docker

### Create Dockerfile

```dockerfile
# Dockerfile
FROM node:18-alpine AS base

# Install dependencies only when needed
FROM base AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app

COPY package.json package-lock.json* ./
RUN npm ci

# Rebuild the source code only when needed
FROM base AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .

# Set environment variables for build
ARG NEXT_PUBLIC_SUPABASE_URL
ARG NEXT_PUBLIC_SUPABASE_ANON_KEY
ARG NEXT_PUBLIC_INFURA_PROJECT_ID
ARG NEXT_PUBLIC_CONTRACT_ADDRESS
ARG NEXT_PUBLIC_API_BASE_URL

ENV NEXT_PUBLIC_SUPABASE_URL=$NEXT_PUBLIC_SUPABASE_URL
ENV NEXT_PUBLIC_SUPABASE_ANON_KEY=$NEXT_PUBLIC_SUPABASE_ANON_KEY
ENV NEXT_PUBLIC_INFURA_PROJECT_ID=$NEXT_PUBLIC_INFURA_PROJECT_ID
ENV NEXT_PUBLIC_CONTRACT_ADDRESS=$NEXT_PUBLIC_CONTRACT_ADDRESS
ENV NEXT_PUBLIC_API_BASE_URL=$NEXT_PUBLIC_API_BASE_URL

RUN npm run build

# Production image
FROM base AS runner
WORKDIR /app

ENV NODE_ENV=production

RUN addgroup --system --gid 1001 nodejs
RUN adduser --system --uid 1001 nextjs

COPY --from=builder /app/public ./public
COPY --from=builder --chown=nextjs:nodejs /app/.next/standalone ./
COPY --from=builder --chown=nextjs:nodejs /app/.next/static ./.next/static

USER nextjs

EXPOSE 3000

ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

CMD ["node", "server.js"]
```

### Create docker-compose.yml

```yaml
version: '3.8'

services:
  stc-iot:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NEXT_PUBLIC_SUPABASE_URL=${NEXT_PUBLIC_SUPABASE_URL}
      - NEXT_PUBLIC_SUPABASE_ANON_KEY=${NEXT_PUBLIC_SUPABASE_ANON_KEY}
      - NEXT_PUBLIC_INFURA_PROJECT_ID=${NEXT_PUBLIC_INFURA_PROJECT_ID}
      - NEXT_PUBLIC_CONTRACT_ADDRESS=${NEXT_PUBLIC_CONTRACT_ADDRESS}
      - JWT_SECRET=${JWT_SECRET}
      - NEXT_PUBLIC_API_BASE_URL=${NEXT_PUBLIC_API_BASE_URL}
    restart: unless-stopped
```

### Build and Run

```bash
# Build image
docker build -t stc-iot-connect .

# Run container
docker run -p 3000:3000 \
  -e NEXT_PUBLIC_SUPABASE_URL=xxx \
  -e NEXT_PUBLIC_SUPABASE_ANON_KEY=xxx \
  -e NEXT_PUBLIC_INFURA_PROJECT_ID=xxx \
  -e NEXT_PUBLIC_CONTRACT_ADDRESS=xxx \
  -e JWT_SECRET=xxx \
  -e NEXT_PUBLIC_API_BASE_URL=xxx \
  stc-iot-connect

# Or use docker-compose
docker-compose up -d
```

---

## ☁️ Deploy to AWS

### Using AWS Amplify

1. **Connect Repository**
   - Go to AWS Amplify Console
   - Click "New app" → "Host web app"
   - Connect your Git repository

2. **Configure Build Settings**
   ```yaml
   version: 1
   frontend:
     phases:
       preBuild:
         commands:
           - npm ci
       build:
         commands:
           - npm run build
     artifacts:
       baseDirectory: .next
       files:
         - '**/*'
     cache:
       paths:
         - node_modules/**/*
   ```

3. **Add Environment Variables**
   - Go to "Environment variables"
   - Add all required variables
   - Save and redeploy

### Using AWS EC2

1. **Launch EC2 Instance**
   ```bash
   # Ubuntu 22.04 LTS
   # t3.medium or larger
   # Security Group: Allow ports 80, 443, 22
   ```

2. **Connect and Setup**
   ```bash
   ssh -i your-key.pem ubuntu@your-ip
   
   # Install Node.js
   curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
   sudo apt-get install -y nodejs
   
   # Install PM2
   sudo npm install -g pm2
   
   # Clone repository
   git clone <your-repo-url>
   cd stc-iot-connect
   
   # Install dependencies
   npm install
   
   # Create .env.local
   nano .env.local
   # Add all environment variables
   
   # Build
   npm run build
   
   # Start with PM2
   pm2 start npm --name "stc-iot" -- start
   pm2 save
   pm2 startup
   ```

3. **Setup Nginx Reverse Proxy**
   ```bash
   sudo apt-get install nginx
   
   # Create config
   sudo nano /etc/nginx/sites-available/stc-iot
   ```
   
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
   
       location / {
           proxy_pass http://localhost:3000;
           proxy_http_version 1.1;
           proxy_set_header Upgrade $http_upgrade;
           proxy_set_header Connection 'upgrade';
           proxy_set_header Host $host;
           proxy_cache_bypass $http_upgrade;
       }
   }
   ```
   
   ```bash
   # Enable site
   sudo ln -s /etc/nginx/sites-available/stc-iot /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   
   # Install SSL with Certbot
   sudo apt-get install certbot python3-certbot-nginx
   sudo certbot --nginx -d your-domain.com
   ```

---

## 🔧 Database Setup in Production

### Supabase Production Setup

1. **Create Production Project**
   - Go to [supabase.com](https://supabase.com)
   - Click "New Project"
   - Choose region close to your users
   - Set strong database password

2. **Run SQL Schema**
   - Go to SQL Editor
   - Copy SQL from README.md
   - Execute all table creation commands

3. **Configure RLS (Row Level Security)**
   ```sql
   -- Enable RLS on all tables
   ALTER TABLE users ENABLE ROW LEVEL SECURITY;
   ALTER TABLE devices ENABLE ROW LEVEL SECURITY;
   ALTER TABLE bookings ENABLE ROW LEVEL SECURITY;
   ALTER TABLE device_events ENABLE ROW LEVEL SECURITY;
   ALTER TABLE webhooks ENABLE ROW LEVEL SECURITY;
   ALTER TABLE audit_logs ENABLE ROW LEVEL SECURITY;
   
   -- Create policies as needed for your security requirements
   ```

4. **Get Production Keys**
   - Go to Settings → API
   - Copy `URL` and `anon/public` key
   - Add to Vercel environment variables

---

## 🔒 Security Configuration

### Enable Rate Limiting

Add to your API routes:

```typescript
// src/middleware.ts
import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

const rateLimit = new Map<string, number[]>();

export function middleware(request: NextRequest) {
  const ip = request.ip ?? 'unknown';
  const now = Date.now();
  const windowMs = 60000; // 1 minute
  const maxRequests = 100;
  
  if (!rateLimit.has(ip)) {
    rateLimit.set(ip, []);
  }
  
  const requests = rateLimit.get(ip)!;
  const recentRequests = requests.filter(time => now - time < windowMs);
  
  if (recentRequests.length >= maxRequests) {
    return NextResponse.json(
      { error: 'Too many requests' },
      { status: 429 }
    );
  }
  
  recentRequests.push(now);
  rateLimit.set(ip, recentRequests);
  
  return NextResponse.next();
}

export const config = {
  matcher: '/api/:path*',
};
```

### Setup CORS

```typescript
// Add to API routes that need CORS
export async function OPTIONS(request: Request) {
  return new Response(null, {
    status: 200,
    headers: {
      'Access-Control-Allow-Origin': 'https://your-domain.com',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    },
  });
}
```

---

## 📊 Monitoring & Logging

### Setup Vercel Analytics

```bash
npm install @vercel/analytics
```

```typescript
// src/app/layout.tsx
import { Analytics } from '@vercel/analytics/react';

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        {children}
        <Analytics />
      </body>
    </html>
  );
}
```

### Setup Error Tracking (Sentry)

```bash
npm install @sentry/nextjs
```

```javascript
// sentry.client.config.js
import * as Sentry from '@sentry/nextjs';

Sentry.init({
  dsn: process.env.NEXT_PUBLIC_SENTRY_DSN,
  tracesSampleRate: 1.0,
  environment: process.env.NODE_ENV,
});
```

---

## 🧪 Testing Production Deploy

### Pre-Launch Tests

```bash
# Test all API endpoints
curl https://your-domain.com/api/health

# Test authentication
curl -X POST https://your-domain.com/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test"}'

# Test device registration
curl -X POST https://your-domain.com/api/device/event \
  -H "Authorization: Bearer stc_xxx..." \
  -H "Content-Type: application/json" \
  -d '{"deviceId":"test-001","type":"qr_scanner"}'

# Test blockchain connection
curl -X POST https://your-domain.com/api/contract/call \
  -H "Authorization: Bearer stc_xxx..." \
  -H "Content-Type: application/json" \
  -d '{"functionName":"testFunction","args":[]}'
```

### Load Testing

```bash
# Install Apache Bench
sudo apt-get install apache2-utils

# Run load test
ab -n 1000 -c 10 https://your-domain.com/api/health

# Install Artillery for advanced testing
npm install -g artillery

# Create load test config
artillery quick --count 10 --num 100 https://your-domain.com/
```

---

## 🔄 Continuous Deployment

### GitHub Actions

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Production

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          
      - name: Install dependencies
        run: npm ci
        
      - name: Run tests
        run: npm test
        
      - name: Build
        run: npm run build
        env:
          NEXT_PUBLIC_SUPABASE_URL: ${{ secrets.SUPABASE_URL }}
          NEXT_PUBLIC_SUPABASE_ANON_KEY: ${{ secrets.SUPABASE_ANON_KEY }}
          
      - name: Deploy to Vercel
        uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.VERCEL_ORG_ID }}
          vercel-project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          vercel-args: '--prod'
```

---

## 📱 Mobile App Deployment (Future)

When building mobile apps with React Native:

1. **iOS App Store**
   - Apple Developer Account required
   - Configure provisioning profiles
   - Submit via Xcode or Transporter

2. **Google Play Store**
   - Google Play Developer Account
   - Generate signed APK
   - Submit via Play Console

3. **Expo (Recommended)**
   ```bash
   npm install -g expo-cli
   expo build:ios
   expo build:android
   ```

---

## 🚨 Rollback Procedures

### Vercel Rollback

1. Go to Vercel Dashboard
2. Click "Deployments"
3. Find previous working deployment
4. Click "..." → "Promote to Production"

### Git Rollback

```bash
# Revert last commit
git revert HEAD
git push

# Or reset to specific commit
git reset --hard <commit-hash>
git push --force
```

---

## 📞 Post-Deployment Support

After successful deployment:

1. ✅ Monitor logs for first 24 hours
2. ✅ Test all critical features
3. ✅ Setup alerts for errors
4. ✅ Document any issues
5. ✅ Update team on deployment status

---

**Deployment Complete! 🎉**

Your STC IoT Connect platform is now live and ready to bridge the physical world with blockchain innovation!
