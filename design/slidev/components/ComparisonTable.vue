<script setup>
defineProps({
  headers: { type: Array, required: true },
  rows: { type: Array, required: true },
  highlightCol: { type: Number, default: -1 },
})
</script>

<template>
  <table class="w-full border-collapse text-[14px]">
    <thead>
      <tr>
        <th v-for="(h, i) in headers" :key="i"
            class="px-[12px] py-[8px] text-left text-[13px] font-semibold text-white"
            style="background-color: var(--color-primary);">
          {{ h }}
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(row, ri) in rows" :key="ri"
          :style="{ backgroundColor: ri % 2 === 1 ? 'var(--color-light-bg)' : 'white' }">
        <td v-for="(cell, ci) in row" :key="ci"
            class="px-[12px] py-[8px]"
            :style="{
              borderBottom: '1px solid var(--color-border)',
              fontWeight: ci === highlightCol ? '700' : '400',
              color: ci === highlightCol ? 'var(--color-primary)' : 'var(--color-text)',
            }">
          {{ cell }}
        </td>
      </tr>
    </tbody>
  </table>
</template>
