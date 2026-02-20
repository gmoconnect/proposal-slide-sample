<template>
  <div class="slidev-layout p-[40px] pb-[48px] h-full flex flex-col">
    <div class="flex-1 grid grid-cols-2 grid-rows-2 gap-[16px] overflow-hidden">
      <div class="border rounded p-[16px]" style="border-color: var(--color-border);">
        <slot name="q1" />
      </div>
      <div class="border rounded p-[16px]" style="border-color: var(--color-border);">
        <slot name="q2" />
      </div>
      <div class="border rounded p-[16px]" style="border-color: var(--color-border);">
        <slot name="q3" />
      </div>
      <div class="border rounded p-[16px]" style="border-color: var(--color-border);">
        <slot name="q4" />
      </div>
    </div>
  </div>
</template>
