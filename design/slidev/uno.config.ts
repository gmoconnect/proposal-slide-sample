import { defineConfig } from 'unocss'

export default defineConfig({
  theme: {
    colors: {
      primary: '#1B3A5C',
      secondary: '#666666',
      accent: '#E63946',
      success: '#2D9C4F',
      muted: '#999999',
      body: '#333333',
      'light-bg': '#F5F7FA',
      border: '#E0E0E0',
    },
  },
  shortcuts: {
    'slide-base': 'p-[40px] font-sans text-body text-[16px] leading-[1.5]',
    'slide-title': 'text-primary font-bold text-[28px] leading-tight',
    'slide-subtitle': 'text-secondary text-[20px]',
    'slide-key-message': 'text-primary text-[20px] font-bold leading-snug',
    'slide-caption': 'text-muted text-[12px]',
    'slide-kpi': 'font-mono text-[48px] font-bold text-primary',
  },
})
