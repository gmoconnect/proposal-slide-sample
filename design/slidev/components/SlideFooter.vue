<script setup>
defineProps({
  source: { type: String, default: '' },
})
</script>

<template>
  <div class="mt-[12px] text-[12px]" style="color: var(--color-muted);">
    <slot />
    <span v-if="source">出所: {{ source }}</span>
  </div>
</template>
