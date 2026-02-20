<script setup>
defineProps({
  cols: { type: Number, default: 3 },
})
</script>

<template>
  <div class="grid gap-[16px]" :style="{ gridTemplateColumns: `repeat(${cols}, 1fr)` }">
    <slot />
  </div>
</template>
