<script setup lang="ts">
import { ref } from "vue";
const props = defineProps(["p", "big"]);
const p = ref(0);
const interval = setInterval(() => {
  if (p.value < props.p) {
    p.value += 2;
  } else {
    clearInterval(interval);
  }
}, 15);
</script>

<template>
  <div
    class="pie"
    :style="
      '--w: ' +
      (big ? 150 : 100) +
      'px;' +
      ';' +
      '--p: ' +
      p +
      '; --b: 10px; --c: #d5b4ff'
    "
  >
    {{ Math.round(p) }}%
  </div>
</template>

<style scoped>
.pie {
  --w: 100px;
  width: var(--w);
  height: var(--w);
  aspect-ratio: 1;
  position: relative;
  display: inline-grid;
  place-content: center;
  margin: 5px;
  font-size: 25px;
  font-weight: bold;
  font-family: sans-serif;
}
.pie:before {
  content: "";
  position: absolute;
  border-radius: 50%;
  inset: 0;
  background: conic-gradient(var(--c) calc(var(--p) * 1%), #0000 0);
  -webkit-mask: radial-gradient(
    farthest-side,
    #0000 calc(99% - var(--b)),
    #000 calc(100% - var(--b))
  );
  mask: radial-gradient(
    farthest-side,
    #0000 calc(99% - var(--b)),
    #000 calc(100% - var(--b))
  );
}
</style>
