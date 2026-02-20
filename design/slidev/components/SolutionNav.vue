<script setup>
defineProps({
  current: { type: Number, default: 0 },
})

const sections = ['全体像', '性能', '拡張性・コスト', 'セキュリティ', '可用性・認証', '可視化']
</script>

<template>
  <div class="flex items-center gap-[3px] flex-wrap mb-[8px]">
    <template v-for="(section, i) in sections" :key="i">
      <div
        class="px-[10px] py-[3px] rounded text-[11px] transition-all"
        :style="{
          backgroundColor: i === current ? 'var(--color-primary)' : 'var(--color-light-bg)',
          color: i === current ? 'white' : 'var(--color-muted)',
          fontWeight: i === current ? '700' : '400',
        }"
      >
        {{ section }}
      </div>
      <div v-if="i < sections.length - 1" class="text-[12px]" style="color: var(--color-border);">
        ›
      </div>
    </template>
  </div>
</template>
