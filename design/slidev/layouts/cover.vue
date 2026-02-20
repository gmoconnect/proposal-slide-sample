<template>
  <div class="slidev-layout h-full flex flex-col justify-center items-center px-[80px] text-white"
       style="background-color: var(--color-primary);">
    <div class="text-center">
      <h1 class="text-[36px] font-bold leading-tight mb-[24px] text-white">
        <slot />
      </h1>
      <div class="text-[20px] opacity-80 mt-[16px]">
        <slot name="subtitle" />
      </div>
    </div>
  </div>
</template>
