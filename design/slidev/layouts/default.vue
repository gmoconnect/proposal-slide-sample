<template>
  <div class="slidev-layout p-[40px] pb-[48px] h-full flex flex-col">
    <div class="flex-1 overflow-hidden text-[16px]">
      <slot />
    </div>
    <div v-if="$slots.footnote" class="flex-shrink-0 mt-[12px] text-[12px]" style="color: var(--color-muted);">
      <slot name="footnote" />
    </div>
  </div>
</template>
