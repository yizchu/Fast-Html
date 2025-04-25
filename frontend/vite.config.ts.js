var __require = /* @__PURE__ */ ((x) => typeof require !== "undefined" ? require : typeof Proxy !== "undefined" ? new Proxy(x, {
  get: (a, b) => (typeof require !== "undefined" ? require : a)[b]
}) : x)(function(x) {
  if (typeof require !== "undefined")
    return require.apply(this, arguments);
  throw new Error('Dynamic require of "' + x + '" is not supported');
});

// vite.config.ts
import { defineConfig, loadEnv } from "vite";
import vue from "@vitejs/plugin-vue";
import { createHtmlPlugin } from "vite-plugin-html";
import vueJsx from "@vitejs/plugin-vue-jsx";
import commonjs from "rollup-plugin-commonjs";
var autoprefixer = __require("autoprefixer");
var path = __require("path");
var config = ({ mode }) => {
  const isProd = mode === "production";
  const envPrefix = "APP_";
  const { APP_TITLE = "" } = loadEnv(mode, process.cwd(), envPrefix);
  return {
    plugins: [
      vue(),
      vueJsx({}),
      createHtmlPlugin({
        minify: isProd,
        inject: {
          data: {
            title: APP_TITLE
          }
        }
      }),
      commonjs({
        extensions: [".js"]
      })
    ],
    build: {
      target: "es2015",
      outDir: path.resolve("C:\\cza\\python_work\\\u81EA\u5B66\u4F5C\u54C1\\fast-html\\frontend", "dist"),
      assetsDir: "assets",
      assetsInlineLimit: 8192,
      sourcemap: !isProd,
      emptyOutDir: true,
      rollupOptions: {
        input: path.resolve("C:\\cza\\python_work\\\u81EA\u5B66\u4F5C\u54C1\\fast-html\\frontend", "index.html"),
        output: {
          chunkFileNames: "js/[name].[hash].js",
          entryFileNames: "js/[name].[hash].js"
        }
      }
    },
    envPrefix,
    resolve: {
      alias: [
        { find: /^@\//, replacement: path.resolve("C:\\cza\\python_work\\\u81EA\u5B66\u4F5C\u54C1\\fast-html\\frontend", "src") + "/" },
        { find: /^~/, replacement: "" }
      ],
      extensions: [".ts", ".tsx", ".js", ".mjs", ".vue", ".json", ".less", ".css"]
    },
    css: {
      postcss: {
        plugins: [
          autoprefixer
        ]
      },
      preprocessorOptions: {
        less: {
          javascriptEnabled: true,
          additionalData: `@import "${path.resolve("C:\\cza\\python_work\\\u81EA\u5B66\u4F5C\u54C1\\fast-html\\frontend", "src/styles/variable.less")}";`
        }
      }
    },
    server: {
      open: false
    },
    preview: {
      port: 5e3
    }
  };
};
var vite_config_default = defineConfig(config);
export {
  vite_config_default as default
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcudHMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImltcG9ydCB7IGRlZmluZUNvbmZpZywgbG9hZEVudiB9IGZyb20gJ3ZpdGUnXG5pbXBvcnQgdnVlIGZyb20gJ0B2aXRlanMvcGx1Z2luLXZ1ZSdcbmltcG9ydCB7IGNyZWF0ZUh0bWxQbHVnaW4gfSBmcm9tICd2aXRlLXBsdWdpbi1odG1sJ1xuaW1wb3J0IHZ1ZUpzeCBmcm9tICdAdml0ZWpzL3BsdWdpbi12dWUtanN4J1xuY29uc3QgYXV0b3ByZWZpeGVyID0gcmVxdWlyZSgnYXV0b3ByZWZpeGVyJylcbmNvbnN0IHBhdGggPSByZXF1aXJlKCdwYXRoJylcbmltcG9ydCBjb21tb25qcyBmcm9tICdyb2xsdXAtcGx1Z2luLWNvbW1vbmpzJztcblxuY29uc3QgY29uZmlnID0gKHsgbW9kZSB9KSA9PiB7XG4gICAgY29uc3QgaXNQcm9kID0gbW9kZSA9PT0gJ3Byb2R1Y3Rpb24nXG4gICAgY29uc3QgZW52UHJlZml4ID0gJ0FQUF8nXG4gICAgY29uc3QgeyBBUFBfVElUTEUgPSAnJyB9ID0gbG9hZEVudihtb2RlLCBwcm9jZXNzLmN3ZCgpLCBlbnZQcmVmaXgpXG4gICAgcmV0dXJuIHtcbiAgICAgICAgcGx1Z2luczogW1xuICAgICAgICAgICAgdnVlKCksXG4gICAgICAgICAgICB2dWVKc3goe1xuICAgICAgICAgICAgICAgIC8vIG9wdGlvbnMgYXJlIHBhc3NlZCBvbiB0byBAdnVlL2JhYmVsLXBsdWdpbi1qc3hcbiAgICAgICAgICAgIH0pLFxuICAgICAgICAgICAgY3JlYXRlSHRtbFBsdWdpbih7XG4gICAgICAgICAgICAgICAgbWluaWZ5OiBpc1Byb2QsXG4gICAgICAgICAgICAgICAgaW5qZWN0OiB7XG4gICAgICAgICAgICAgICAgICAgIGRhdGE6IHtcbiAgICAgICAgICAgICAgICAgICAgICAgIHRpdGxlOiBBUFBfVElUTEUsXG4gICAgICAgICAgICAgICAgICAgIH0sXG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgfSksXG4gICAgICAgICAgICBjb21tb25qcyh7XG4gICAgICAgICAgICAgICAgZXh0ZW5zaW9uczogWycuanMnXVxuICAgICAgICAgICAgfSksXG4gICAgICAgIF0sXG4gICAgICAgIGJ1aWxkOiB7XG4gICAgICAgICAgICB0YXJnZXQ6ICdlczIwMTUnLFxuICAgICAgICAgICAgb3V0RGlyOiBwYXRoLnJlc29sdmUoXCJDOlxcXFxjemFcXFxccHl0aG9uX3dvcmtcXFxcXHU4MUVBXHU1QjY2XHU0RjVDXHU1NEMxXFxcXGZhc3QtaHRtbFxcXFxmcm9udGVuZFwiLCAnZGlzdCcpLFxuICAgICAgICAgICAgYXNzZXRzRGlyOiAnYXNzZXRzJyxcbiAgICAgICAgICAgIGFzc2V0c0lubGluZUxpbWl0OiA4MTkyLFxuICAgICAgICAgICAgc291cmNlbWFwOiAhaXNQcm9kLFxuICAgICAgICAgICAgZW1wdHlPdXREaXI6IHRydWUsXG4gICAgICAgICAgICByb2xsdXBPcHRpb25zOiB7XG4gICAgICAgICAgICAgICAgaW5wdXQ6IHBhdGgucmVzb2x2ZShcIkM6XFxcXGN6YVxcXFxweXRob25fd29ya1xcXFxcdTgxRUFcdTVCNjZcdTRGNUNcdTU0QzFcXFxcZmFzdC1odG1sXFxcXGZyb250ZW5kXCIsICdpbmRleC5odG1sJyksXG4gICAgICAgICAgICAgICAgb3V0cHV0OiB7XG4gICAgICAgICAgICAgICAgICAgIGNodW5rRmlsZU5hbWVzOiAnanMvW25hbWVdLltoYXNoXS5qcycsXG4gICAgICAgICAgICAgICAgICAgIGVudHJ5RmlsZU5hbWVzOiAnanMvW25hbWVdLltoYXNoXS5qcycsXG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgfVxuICAgICAgICB9LFxuICAgICAgICBlbnZQcmVmaXgsXG4gICAgICAgIHJlc29sdmU6IHtcbiAgICAgICAgICAgIGFsaWFzOiBbXG4gICAgICAgICAgICAgICAgeyBmaW5kOiAvXkBcXC8vLCByZXBsYWNlbWVudDogcGF0aC5yZXNvbHZlKFwiQzpcXFxcY3phXFxcXHB5dGhvbl93b3JrXFxcXFx1ODFFQVx1NUI2Nlx1NEY1Q1x1NTRDMVxcXFxmYXN0LWh0bWxcXFxcZnJvbnRlbmRcIiwgJ3NyYycpICsgJy8nIH0sXG4gICAgICAgICAgICAgICAgeyBmaW5kOiAvXn4vLCByZXBsYWNlbWVudDogJycgfVxuICAgICAgICAgICAgXSxcbiAgICAgICAgICAgIGV4dGVuc2lvbnM6IFsnLnRzJywgJy50c3gnLCAnLmpzJywgJy5tanMnLCAnLnZ1ZScsICcuanNvbicsICcubGVzcycsICcuY3NzJ11cbiAgICAgICAgfSxcbiAgICAgICAgY3NzOiB7XG4gICAgICAgICAgICBwb3N0Y3NzOiB7XG4gICAgICAgICAgICAgICAgcGx1Z2luczogW1xuICAgICAgICAgICAgICAgICAgICBhdXRvcHJlZml4ZXJcbiAgICAgICAgICAgICAgICBdLFxuICAgICAgICAgICAgfSxcbiAgICAgICAgICAgIHByZXByb2Nlc3Nvck9wdGlvbnM6IHtcbiAgICAgICAgICAgICAgICBsZXNzOiB7XG4gICAgICAgICAgICAgICAgICAgIGphdmFzY3JpcHRFbmFibGVkOiB0cnVlLFxuICAgICAgICAgICAgICAgICAgICBhZGRpdGlvbmFsRGF0YTogYEBpbXBvcnQgXCIke3BhdGgucmVzb2x2ZShcIkM6XFxcXGN6YVxcXFxweXRob25fd29ya1xcXFxcdTgxRUFcdTVCNjZcdTRGNUNcdTU0QzFcXFxcZmFzdC1odG1sXFxcXGZyb250ZW5kXCIsICdzcmMvc3R5bGVzL3ZhcmlhYmxlLmxlc3MnKX1cIjtgXG4gICAgICAgICAgICAgICAgfVxuICAgICAgICAgICAgfVxuICAgICAgICB9LFxuICAgICAgICBzZXJ2ZXI6IHtcbiAgICAgICAgICAgIG9wZW46IGZhbHNlXG4gICAgICAgIH0sXG4gICAgICAgIHByZXZpZXc6IHtcbiAgICAgICAgICAgIHBvcnQ6IDUwMDBcbiAgICAgICAgfSxcblxuICAgIH1cbn1cblxuZXhwb3J0IGRlZmF1bHQgZGVmaW5lQ29uZmlnKGNvbmZpZylcbiJdLAogICJtYXBwaW5ncyI6ICI7Ozs7Ozs7OztBQUFBLFNBQVMsY0FBYyxlQUFlO0FBQ3RDLE9BQU8sU0FBUztBQUNoQixTQUFTLHdCQUF3QjtBQUNqQyxPQUFPLFlBQVk7QUFHbkIsT0FBTyxjQUFjO0FBRnJCLElBQU0sZUFBZSxVQUFRO0FBQzdCLElBQU0sT0FBTyxVQUFRO0FBR3JCLElBQU0sU0FBUyxDQUFDLEVBQUUsS0FBSyxNQUFNO0FBQ3pCLFFBQU0sU0FBUyxTQUFTO0FBQ3hCLFFBQU0sWUFBWTtBQUNsQixRQUFNLEVBQUUsWUFBWSxHQUFHLElBQUksUUFBUSxNQUFNLFFBQVEsSUFBSSxHQUFHLFNBQVM7QUFDakUsU0FBTztBQUFBLElBQ0gsU0FBUztBQUFBLE1BQ0wsSUFBSTtBQUFBLE1BQ0osT0FBTyxDQUVQLENBQUM7QUFBQSxNQUNELGlCQUFpQjtBQUFBLFFBQ2IsUUFBUTtBQUFBLFFBQ1IsUUFBUTtBQUFBLFVBQ0osTUFBTTtBQUFBLFlBQ0YsT0FBTztBQUFBLFVBQ1g7QUFBQSxRQUNKO0FBQUEsTUFDSixDQUFDO0FBQUEsTUFDRCxTQUFTO0FBQUEsUUFDTCxZQUFZLENBQUMsS0FBSztBQUFBLE1BQ3RCLENBQUM7QUFBQSxJQUNMO0FBQUEsSUFDQSxPQUFPO0FBQUEsTUFDSCxRQUFRO0FBQUEsTUFDUixRQUFRLEtBQUssUUFBUSx1RUFBbUQsTUFBTTtBQUFBLE1BQzlFLFdBQVc7QUFBQSxNQUNYLG1CQUFtQjtBQUFBLE1BQ25CLFdBQVcsQ0FBQztBQUFBLE1BQ1osYUFBYTtBQUFBLE1BQ2IsZUFBZTtBQUFBLFFBQ1gsT0FBTyxLQUFLLFFBQVEsdUVBQW1ELFlBQVk7QUFBQSxRQUNuRixRQUFRO0FBQUEsVUFDSixnQkFBZ0I7QUFBQSxVQUNoQixnQkFBZ0I7QUFBQSxRQUNwQjtBQUFBLE1BQ0o7QUFBQSxJQUNKO0FBQUEsSUFDQTtBQUFBLElBQ0EsU0FBUztBQUFBLE1BQ0wsT0FBTztBQUFBLFFBQ0gsRUFBRSxNQUFNLFFBQVEsYUFBYSxLQUFLLFFBQVEsdUVBQW1ELEtBQUssSUFBSSxJQUFJO0FBQUEsUUFDMUcsRUFBRSxNQUFNLE1BQU0sYUFBYSxHQUFHO0FBQUEsTUFDbEM7QUFBQSxNQUNBLFlBQVksQ0FBQyxPQUFPLFFBQVEsT0FBTyxRQUFRLFFBQVEsU0FBUyxTQUFTLE1BQU07QUFBQSxJQUMvRTtBQUFBLElBQ0EsS0FBSztBQUFBLE1BQ0QsU0FBUztBQUFBLFFBQ0wsU0FBUztBQUFBLFVBQ0w7QUFBQSxRQUNKO0FBQUEsTUFDSjtBQUFBLE1BQ0EscUJBQXFCO0FBQUEsUUFDakIsTUFBTTtBQUFBLFVBQ0YsbUJBQW1CO0FBQUEsVUFDbkIsZ0JBQWdCLFlBQVksS0FBSyxRQUFRLHVFQUFtRCwwQkFBMEI7QUFBQSxRQUMxSDtBQUFBLE1BQ0o7QUFBQSxJQUNKO0FBQUEsSUFDQSxRQUFRO0FBQUEsTUFDSixNQUFNO0FBQUEsSUFDVjtBQUFBLElBQ0EsU0FBUztBQUFBLE1BQ0wsTUFBTTtBQUFBLElBQ1Y7QUFBQSxFQUVKO0FBQ0o7QUFFQSxJQUFPLHNCQUFRLGFBQWEsTUFBTTsiLAogICJuYW1lcyI6IFtdCn0K
