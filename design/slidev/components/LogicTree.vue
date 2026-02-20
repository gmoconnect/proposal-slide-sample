<script setup>
defineProps({
  tree: { type: Object, required: true },
})
</script>

<template>
  <div class="flex items-start gap-[16px]">
    <!-- Root node -->
    <div class="rounded-lg p-[12px] text-white text-[14px] font-bold min-w-[120px] text-center flex-shrink-0"
         style="background-color: var(--color-primary);">
      {{ tree.label }}
    </div>
    <!-- Children -->
    <div v-if="tree.children" class="flex flex-col gap-[8px]">
      <div v-for="(child, i) in tree.children" :key="i" class="flex items-start gap-[12px]">
        <div class="text-[18px] mt-[6px] flex-shrink-0" style="color: var(--color-primary);">&rarr;</div>
        <div class="border rounded-lg p-[10px] min-w-[100px]" style="border-color: var(--color-border);">
          <div class="text-[13px] font-bold" style="color: var(--color-primary);">{{ child.label }}</div>
          <div v-if="child.detail" class="text-[11px] mt-[2px]" style="color: var(--color-secondary);">{{ child.detail }}</div>
        </div>
        <!-- Grandchildren -->
        <template v-if="child.children">
          <div v-for="(gc, j) in child.children" :key="j" class="flex items-center gap-[8px]">
            <div class="text-[14px]" style="color: var(--color-muted);">&rarr;</div>
            <div class="rounded px-[8px] py-[4px] text-[11px]" style="background-color: var(--color-light-bg); color: var(--color-text);">
              {{ gc.label }}
            </div>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>
