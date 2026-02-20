<template>
  <div class="slidev-layout p-[40px] pb-[48px] h-full flex flex-col">
    <div class="flex-1 grid grid-cols-2 gap-[24px] overflow-hidden">
      <div class="overflow-hidden">
        <slot />
      </div>
      <div class="overflow-hidden">
        <slot name="right" />
      </div>
    </div>
  </div>
</template>
