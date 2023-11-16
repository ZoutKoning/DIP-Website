const express = require('express');
const axios = require('axios');
const cors = require('cors');
const app = express();

app.use(cors());

const options = {
  method: 'GET',
  url: 'https://ebay-search-result.p.rapidapi.com/search/iphone',
  headers: {
    'X-RapidAPI-Key': '5312141f13mshf56b15461559508p1b3ee1jsna43bf4b24cc7',
    'X-RapidAPI-Host': 'ebay-search-result.p.rapidapi.com'
  }
};

app.get('/api/products', async (req, res) => {
  try {
    const response = await axios.request(options);
    res.json(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).send('Error fetching products');
  }
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
