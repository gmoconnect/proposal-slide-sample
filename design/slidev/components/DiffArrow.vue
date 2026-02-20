<script setup>
defineProps({
  label: { type: String, required: true },
  positive: { type: Boolean, default: true },
})
</script>

<template>
  <span class="inline-flex items-center gap-[4px] font-bold text-[14px]"
        :style="{ color: positive ? 'var(--color-success)' : 'var(--color-accent)' }">
    <span>{{ positive ? '▲' : '▼' }}</span>
    <span>{{ label }}</span>
  </span>
</template>
