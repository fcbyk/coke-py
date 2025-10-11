import DefaultTheme from 'vitepress/theme'
import PasswordProtected from '../components/PasswordProtected.vue'
import type { EnhanceAppContext } from 'vitepress'
import { CCollapse, CBadge, CCollapseGroup } from '@fcbyk/vue-ui'
import CokeUI from '@fcbyk/vue-ui'
import '@fcbyk/vue-ui/style.css'


export default {
  ...DefaultTheme,
  enhanceApp(ctx: EnhanceAppContext) {
    DefaultTheme.enhanceApp(ctx)
    ctx.app.component('pd', PasswordProtected)
    ctx.app.component('qa', CCollapse)
    ctx.app.component('qa-g', CCollapseGroup)
    // 注册组件库
    ctx.app.use(CokeUI)
  }
}