const express = require('express');
const cors = require('cors');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

// Route de santé
app.get('/health', (req, res) => {
    res.json({
        status: '🟢 OK',
        service: 'MSY API Core',
        timestamp: new Date().toISOString(),
        version: '1.0.0'
    });
});

// Route principale
app.get('/api', (req, res) => {
    res.json({
        message: '🏛️ Bienvenue sur MSY INT API',
        philosophy: 'Nous ne sommes pas des concurrents mais des contributeurs',
        hierarchy: 'Niveau 2 - Coordination Opérationnelle'
    });
});

app.listen(PORT, '0.0.0.0', () => {
    console.log(`🏛️ MSY API démarrée sur le port ${PORT}`);
});
