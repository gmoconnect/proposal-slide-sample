<template>
  <footer
    v-if="$slidev.nav.currentLayout !== 'cover' && $slidev.nav.currentLayout !== 'section'"
    class="absolute bottom-0 left-0 right-0 px-[40px] pb-[12px] flex justify-between items-end text-[11px]"
    style="color: var(--color-muted);"
  >
    <span>{{ $slidev.configs.title }}</span>
    <span style="font-family: var(--font-number);">
      {{ $slidev.nav.currentPage }} / {{ $slidev.nav.total }}
    </span>
  </footer>
</template>
