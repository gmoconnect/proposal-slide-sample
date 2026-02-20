<script setup>
defineProps({
  beforeLabel: { type: String, default: 'Before' },
  afterLabel: { type: String, default: 'After' },
  improvement: { type: String, default: '' },
})
</script>

<template>
  <div class="grid gap-[16px] items-stretch" style="grid-template-columns: 1fr auto 1fr;">
    <div class="border rounded-lg p-[20px]"
         style="border-color: var(--color-border); background-color: var(--color-light-bg);">
      <div class="font-bold text-[14px] mb-[12px]" style="color: var(--color-secondary);">{{ beforeLabel }}</div>
      <slot name="before" />
    </div>
    <div class="flex flex-col items-center justify-center">
      <div class="text-[32px]" style="color: var(--color-primary);">&rarr;</div>
      <div v-if="improvement" class="font-bold text-[14px] mt-[4px]" style="color: var(--color-accent);">
        {{ improvement }}
      </div>
    </div>
    <div class="border-2 rounded-lg p-[20px]"
         style="border-color: var(--color-primary); background: white;">
      <div class="font-bold text-[14px] mb-[12px]" style="color: var(--color-primary);">{{ afterLabel }}</div>
      <slot name="after" />
    </div>
  </div>
</template>
