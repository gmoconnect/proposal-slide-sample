<script setup>
defineProps({
  sections: { type: Array, required: true },
  current: { type: Number, default: 0 },
})
</script>

<template>
  <div class="flex items-center gap-[4px] flex-wrap">
    <template v-for="(section, i) in sections" :key="i">
      <div
        class="px-[16px] py-[12px] rounded text-[14px] transition-all"
        :style="{
          backgroundColor: i === current ? 'var(--color-primary)' : 'var(--color-light-bg)',
          color: i === current ? 'white' : 'var(--color-secondary)',
          fontWeight: i === current ? '700' : '400',
        }"
      >
        {{ section }}
      </div>
      <div v-if="i < sections.length - 1" class="text-[20px]" style="color: var(--color-muted);">
        &rarr;
      </div>
    </template>
  </div>
</template>
