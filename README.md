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

- **Git** - Version control
- **Node.js 18+** 
- **npm**

#### Installing Git

**macOS:**
```bash
brew install git
```

**Linux (Debian/Ubuntu):**
```bash
sudo apt update
sudo apt install git
```

**Linux (Fedora):**
```bash
sudo dnf install git
```

**Windows:**
Download from https://git-scm.com

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

### Running Multiple Pages

This project uses Vite's multi-page setup. Both pages are served from the same development server:

| URL | Description |
|-----|-------------|
| `http://localhost:5000/` | Main index.html |
| `http://localhost:5000/versiononeernesto.html` | Alternative version |

### Build

```bash
npm run build
```

The build output will include both pages in the `dist/` folder.

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
