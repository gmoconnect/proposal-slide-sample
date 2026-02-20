<script setup>
defineProps({
  steps: { type: Array, required: true },
})
</script>

<template>
  <div class="flex items-center justify-center gap-[4px] w-full">
    <template v-for="(step, i) in steps" :key="i">
      <div class="flex-1 rounded-lg p-[16px] text-center text-white min-w-0"
           style="background-color: var(--color-primary);">
        <div class="font-bold text-[14px]">{{ step.label }}</div>
        <div v-if="step.description" class="text-[12px] opacity-80 mt-[4px]">{{ step.description }}</div>
      </div>
      <div v-if="i < steps.length - 1" class="text-[24px] flex-shrink-0" style="color: var(--color-primary);">
        &rarr;
      </div>
    </template>
  </div>
</template>
