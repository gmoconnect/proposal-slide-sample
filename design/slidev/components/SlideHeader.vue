<script setup>
defineProps({
  subtitle: { type: String, default: '' },
})
</script>

<template>
  <div class="mb-[24px]">
    <h2 class="text-[20px] font-bold leading-snug" style="color: var(--color-primary);">
      <slot />
    </h2>
    <p v-if="subtitle" class="text-[16px] mt-[8px]" style="color: var(--color-secondary);">
      {{ subtitle }}
    </p>
  </div>
</template>
