<script setup>
defineProps({
  xLabel: { type: String, default: '' },
  yLabel: { type: String, default: '' },
  xLow: { type: String, default: '低' },
  xHigh: { type: String, default: '高' },
  yLow: { type: String, default: '低' },
  yHigh: { type: String, default: '高' },
})
</script>

<template>
  <div class="flex items-stretch gap-[8px]">
    <!-- Y-axis label -->
    <div class="flex flex-col justify-center items-center w-[24px]">
      <span class="text-[12px] font-bold writing-vertical-lr" style="color: var(--color-secondary);">{{ yLabel }}</span>
    </div>
    <div class="flex-1">
      <!-- Y high label -->
      <div class="text-[11px] mb-[4px]" style="color: var(--color-muted);">{{ yHigh }} &uarr;</div>
      <!-- Matrix grid -->
      <div class="grid grid-cols-2 grid-rows-2 gap-[8px]">
        <div class="border rounded p-[12px] min-h-[100px]" style="border-color: var(--color-border);">
          <slot name="q1" />
        </div>
        <div class="border rounded p-[12px] min-h-[100px]" style="border-color: var(--color-border);">
          <slot name="q2" />
        </div>
        <div class="border rounded p-[12px] min-h-[100px]" style="border-color: var(--color-border);">
          <slot name="q3" />
        </div>
        <div class="border rounded p-[12px] min-h-[100px]" style="border-color: var(--color-border);">
          <slot name="q4" />
        </div>
      </div>
      <!-- X-axis labels -->
      <div class="flex justify-between mt-[4px]">
        <span class="text-[11px]" style="color: var(--color-muted);">{{ xLow }}</span>
        <span class="text-[12px] font-bold" style="color: var(--color-secondary);">{{ xLabel }}</span>
        <span class="text-[11px]" style="color: var(--color-muted);">{{ xHigh }} &rarr;</span>
      </div>
    </div>
  </div>
</template>
