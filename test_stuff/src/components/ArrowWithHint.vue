<script>
import arrowIconLeft from './icons/arrowIconLeft.vue';
export default {
    components: {
        arrowIconLeft,
    },
    props: {
        isMirrored: Boolean,
        right: Number
    },
    computed: {
        svgStyle() {
            return  {
                transform: this.isMirrored ? 'scale(-1,1)': 'none',
                width: '50%'
            }
        },
        spanStyle() {
            return {
                position: "relative",
                right: `${this.right}` + "%",
            }
        }
    }
}
</script>
<template>
    <div class="container">
        <span :style="spanStyle">
            <slot />
        </span>
        <arrowIconLeft :style="svgStyle" ref="arrowSVG"/>
    </div>
</template>

<style>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
}
</style>