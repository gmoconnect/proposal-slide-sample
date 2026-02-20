<script setup>
defineProps({
  color: { type: String, default: 'primary' },
})

const colorMap = {
  primary: { bg: 'var(--color-primary)', text: 'white' },
  accent: { bg: 'var(--color-accent)', text: 'white' },
  success: { bg: 'var(--color-success)', text: 'white' },
  muted: { bg: 'var(--color-light-bg)', text: 'var(--color-secondary)' },
}
</script>

<template>
  <span class="inline-block px-[8px] py-[2px] rounded text-[12px] font-bold"
        :style="{
          backgroundColor: colorMap[color]?.bg || colorMap.primary.bg,
          color: colorMap[color]?.text || colorMap.primary.text,
        }">
    <slot />
  </span>
</template>
