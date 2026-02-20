<template>
  <div class="slidev-layout h-full flex flex-col justify-center px-[80px] text-white"
       style="background-color: var(--color-primary);">
    <div class="text-[14px] uppercase tracking-widest opacity-60 mb-[16px]">
      <slot name="label" />
    </div>
    <h1 class="text-[36px] font-bold leading-tight text-white">
      <slot />
    </h1>
  </div>
</template>
