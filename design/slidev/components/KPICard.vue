<script setup>
defineProps({
  value: { type: String, required: true },
  label: { type: String, required: true },
  unit: { type: String, default: '' },
  change: { type: String, default: '' },
  positive: { type: Boolean, default: true },
})
</script>

<template>
  <div class="text-center p-[24px]">
    <div class="font-bold leading-none" style="font-family: var(--font-number); font-size: var(--font-size-kpi); color: var(--color-primary);">
      {{ value }}<span v-if="unit" class="text-[24px] ml-[4px]">{{ unit }}</span>
    </div>
    <div class="text-[14px] mt-[8px]" style="color: var(--color-secondary);">{{ label }}</div>
    <div
      v-if="change"
      class="text-[14px] font-bold mt-[4px]"
      :style="{ color: positive ? 'var(--color-success)' : 'var(--color-accent)' }"
    >
      {{ change }}
    </div>
  </div>
</template>
