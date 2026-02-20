<script setup>
defineProps({
  phases: { type: Array, required: true },
  months: { type: Number, default: 6 },
})
</script>

<template>
  <div class="w-full">
    <!-- Month headers -->
    <div class="grid gap-[2px] mb-[8px]" :style="{ gridTemplateColumns: `120px repeat(${months}, 1fr)` }">
      <div></div>
      <div v-for="m in months" :key="m" class="text-center text-[12px] font-bold" style="color: var(--color-secondary);">
        {{ m }}ヶ月目
      </div>
    </div>
    <!-- Phase bars -->
    <div v-for="(phase, i) in phases" :key="i"
         class="grid gap-[2px] mb-[4px]"
         :style="{ gridTemplateColumns: `120px repeat(${months}, 1fr)` }">
      <div class="text-[12px] font-bold pr-[8px] flex items-center" style="color: var(--color-primary);">
        {{ phase.label }}
      </div>
      <template v-for="m in months" :key="m">
        <div
          class="h-[28px] rounded-sm"
          :style="{
            backgroundColor: m >= phase.start && m <= phase.end ? 'var(--color-primary)' : 'var(--color-light-bg)',
            opacity: m >= phase.start && m <= phase.end ? 1 : 0.3,
          }"
        ></div>
      </template>
    </div>
  </div>
</template>
