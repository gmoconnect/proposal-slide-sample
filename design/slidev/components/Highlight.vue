<script setup>
defineProps({
  color: { type: String, default: 'accent' },
})

const colorMap = {
  primary: 'var(--color-primary)',
  accent: 'var(--color-accent)',
  success: 'var(--color-success)',
}
</script>

<template>
  <span class="font-bold" :style="{ color: colorMap[color] || colorMap.accent }">
    <slot />
  </span>
</template>
