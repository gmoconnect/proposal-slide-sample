<script setup>
defineProps({
  type: { type: String, default: 'info' },
})

const styles = {
  info: { borderColor: 'var(--color-primary)', bg: '#EBF0F7' },
  warning: { borderColor: 'var(--color-accent)', bg: '#FEF2F2' },
  success: { borderColor: 'var(--color-success)', bg: '#ECFDF5' },
}
</script>

<template>
  <div class="border-l-4 rounded-r px-[16px] py-[12px] text-[14px] [&>p]:my-0"
       :style="{
         borderLeftColor: styles[type]?.borderColor || styles.info.borderColor,
         backgroundColor: styles[type]?.bg || styles.info.bg,
       }">
    <slot />
  </div>
</template>
