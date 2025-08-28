const express = require('express');
const path = require('path');
const app = express();


// Serve static files (our HTML form)
app.use(express.static(path.join(__dirname, 'public')));


// Health check
app.get('/health', (_req, res) => {
res.json({ service: 'express-frontend', status: 'ok' });
});


const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`Frontend listening on http://localhost:${PORT}`));