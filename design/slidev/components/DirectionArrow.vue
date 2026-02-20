<script setup>
defineProps({
  direction: { type: String, default: 'right' },
  size: { type: String, default: 'md' },
})

const arrows = { right: '→', left: '←', up: '↑', down: '↓' }
const sizes = { sm: '16px', md: '24px', lg: '36px' }
</script>

<template>
  <span class="inline-block font-bold"
        :style="{ fontSize: sizes[size], color: 'var(--color-primary)' }">
    {{ arrows[direction] || arrows.right }}
  </span>
</template>
