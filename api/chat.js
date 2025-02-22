export default async function handler(req, res) {
    if (req.method !== 'POST') {
        return res.status(405).json({ message: 'Method Not Allowed' });
    }

    const { message } = req.body;
    const apiKey = process.env.OPENAI_API_KEY; // Store your API key in Vercel environment variables

    try {
        const response = await fetch('https://api.openai.com/v1/chat/completions', {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${apiKey}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                model: 'gpt-3.5-turbo', // Change to "gpt-4" if needed
                messages: [{ role: 'user', content: message }],
            }),
        });

        const data = await response.json();
        res.status(200).json({ reply: data.choices[0].message.content });
    } catch (error) {
        res.status(500).json({ error: 'Error fetching response from OpenAI' });
    }
}
