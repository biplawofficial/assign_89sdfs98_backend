// server.js
const express = require('express');
const LangflowClient = require('./langflowClient');
const config = require('./config');
const cors = require('cors');
const app = express();



app.use(cors({
  origin: 'https://assign-89sdf98-wrgr.vercel.app/aboutus', // Replace with your frontend URL
}));
app.use(cors())
app.use(express.json());

// Initialize LangFlow client
const langflowClient = new LangflowClient(
    config.LANGFLOW_BASE_URL,
    config.APPLICATION_TOKEN
);

// Health check endpoint
app.get('/health', (req, res) => {
    res.json({ status: 'OK' });
});

// Main API endpoint for processing messages
app.post('/api/process', async (req, res) => {
    try {
        const { 
            message, 
            inputType = 'chat', 
            outputType = 'chat', 
            stream = false 
        } = req.body;

        if (!message) {
            return res.status(400).json({ error: 'Message is required' });
        }

        const response = await langflowClient.runFlow(
            config.FLOW_ID,
            config.LANGFLOW_ID,
            message,
            inputType,
            outputType,
            config.TWEAKS,
            stream,
            (data) => console.log("Received:", data.chunk),
            (message) => console.log("Stream Closed:", message),
            (error) => console.log("Stream Error:", error)
        );

        if (!stream && response && response.outputs) {
            const output = response.outputs[0].outputs[0].outputs.message;
            return res.json({ response: output.message.text });
        }

        // Handle streaming response
        if (stream) {
            // Set headers for SSE
            res.writeHead(200, {
                'Content-Type': 'text/event-stream',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive'
            });

            // Handle streaming data
            response.on('data', (chunk) => {
                res.write(`data: ${JSON.stringify(chunk)}\n\n`);
            });

            response.on('end', () => {
                res.end();
            });
        }

    } catch (error) {
        console.error('Error processing request:', error);
        res.status(500).json({ error: 'Internal server error', details: error.message });
    }
});

// Start the server
app.listen(config.PORT, () => {
    console.log(`Server running on port ${config.PORT}`);
});
