// src/plugins/vuetify.js
import 'vuetify/styles'; // Importa os estilos globais do Vuetify
import { createVuetify } from 'vuetify';
import { mdi } from 'vuetify/iconsets/mdi'; // Ícones Material Design

export default createVuetify({
  icons: {
    defaultSet: 'mdi',
    sets: { mdi },
  },
  theme: {
    defaultTheme: 'light',
    themes: {
      light: {
        colors: {
          primary: '#1976D2',
          secondary: '#424242',
        },
      },
    },
  },
});
