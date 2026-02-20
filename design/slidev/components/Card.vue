<script setup>
defineProps({
  title: { type: String, default: '' },
  icon: { type: String, default: '' },
})
</script>

<template>
  <div class="border rounded-lg p-[20px]"
       style="border-color: var(--color-border); background: white;">
    <div v-if="icon" class="text-[24px] mb-[8px]">{{ icon }}</div>
    <div v-if="title" class="font-bold text-[16px] mb-[8px]" style="color: var(--color-primary);">
      {{ title }}
    </div>
    <div class="text-[14px] leading-relaxed" style="color: var(--color-text);">
      <slot />
    </div>
  </div>
</template>
