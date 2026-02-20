<script setup>
defineProps({
  sections: { type: Array, default: () => [] },
  current: { type: Number, default: 0 },
})
</script>

<template>
  <div class="slidev-layout p-[40px] pb-[48px] h-full flex flex-col">
    <h2 class="text-[28px] font-bold mb-[32px]" style="color: var(--color-primary);">
      アジェンダ
    </h2>
    <div class="flex-1 flex flex-col justify-center">
      <SectionNav v-if="sections.length" :sections="sections" :current="current" />
      <slot />
    </div>
  </div>
</template>
