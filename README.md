# Ernesto Kitchen

Filipino home cooking website for Ernesto Kitchen, a Filipino restaurant in Calgary, AB.

## About

Authentic Filipino home cooking made with love. Every dish is made from scratch using traditional recipes passed down through generations.

## Tech Stack

- **HTML5** - Semantic markup
- **CSS3** - Custom styling with CSS variables
- **Vite** - Development server and build tool
- **Vanilla JavaScript** - Minimal interactivity

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ernesto_kitchen_website
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start development server**
   ```bash
   npm run dev
   ```

4. **Open in browser**
   Visit `http://localhost:5000`

### Development

```bash
npm run dev
```

The site will be available at `http://localhost:5000`

### Running Multiple Versions

This project supports running two different HTML versions:

| Command | Description | Port |
|---------|-------------|------|
| `npm run dev` | Runs index.html (main version) | 5000 |
| `npm run dev:versionone` | Runs versiononeernesto.html | 5001 |

Both versions can run simultaneously on different ports.

### Build

```bash
npm run build
```

### Build Specific Version

```bash
npm run build        # builds index.html
npm run build:versionone  # builds versiononeernesto.html
```

### Preview Production Build

```bash
npm run preview
```

## Features

- Responsive design
- Mobile-friendly navigation with drawer menu
- Sticky category navigation
- Accordion-style menu categories
- Animated elements
- SEO optimized with structured data

## Deployment

The site can be deployed to any static hosting service:

### GitHub Pages
```bash
npm run build
# Upload dist/ folder to GitHub Pages
```

### Netlify / Vercel
Connect your GitHub repository and it will auto-deploy on push.

## License

Private - All rights reserved.
