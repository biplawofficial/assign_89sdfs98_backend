// config.js
require('dotenv').config();

const config = {
    PORT: process.env.PORT || 3000,
    LANGFLOW_BASE_URL: 'https://api.langflow.astra.datastax.com',
    APPLICATION_TOKEN: process.env.APPLICATION_TOKEN,
    FLOW_ID: 'd343821e-7751-4215-8afd-11f1071fd651',
    LANGFLOW_ID: '486732ff-a748-4b68-a48b-e617028e9db9',
    TWEAKS: {
        "File-jxj7K": {},
        "SplitText-7gH6I": {},
        "ChatInput-Rpb6P": {},
        "ParseData-EJyoR": {},
        "CombineText-GqK4e": {},
        "TextInput-OUxuk": {},
        "ChatOutput-EPD4q": {},
        "AstraDB-brZ4Z": {},
        "GroqModel-SGvGQ": {}
    }
};

module.exports = config;