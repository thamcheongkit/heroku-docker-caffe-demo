<h1>Caffe Flickr Style on Heroku Docker</h1>
<h3>Style classification web service demo</h3>

<hr>

<p>Example <code>POST</code> request:</p>
<code>curl -H "Content-Type: application/json" -X POST \ <br> -d '{"urls":["https://upload.wikimedia.org/wikipedia/en/2/24/Lenna.png"]}' \ <br> -L https://heroku-caffe-test-ck.herokuapp.com/classify</code>
<p>Result:</p>
<code>{"predictions": [1]}</code>

<hr>

<h3>Installation (prerequisite: Have <a href="https://devcenter.heroku.com/articles/heroku-cli">heroku-cli</a> and <a href="https://www.google.com/search?q=docker+install&oq=docker+install&aqs=chrome..69i57j69i65j69i59.1587j0j4&sourceid=chrome&ie=UTF-8">Docker</a> installed):</h3>
<p><code>$ heroku plugins:install heroku-container-registry</code></p>
<p><code>$ git clone https://github.com/thamcheongkit/heroku-docker-caffe-demo.git</code></p>
<p><code>$ cd heroku-docker-caffe-demo</code></p>
<p><code>$ ./api-server/download-pretrained-model.sh</code></p>
<p><code>$ heroku create</code></p>
<p><code>$ heroku container:push web</code></p>
<p><code>$ heroku ps:scale web=1</code></p>
<p>*tips: patient</p>

<hr>

<p>Reference:</p>
<a href="https://devcenter.heroku.com/articles/container-registry-and-runtimedocker">https://devcenter.heroku.com/articles/container-registry-and-runtime</a>
<a href="https://github.com/BVLC/caffe/tree/master/docker">https://github.com/BVLC/caffe/tree/master/docker</a>
<a href="https://github.com/BVLC/caffe/tree/master/examples/finetune_flickr_style">https://github.com/BVLC/caffe/tree/master/examples/finetune_flickr_style</a>
<p>Styles list (from 0 to 19):</p>
<ul>
  <li>Detailed</li>
  <li>Pastel</li>
  <li>Melancholy</li>
  <li>Noir</li>
  <li>HDR</li>
  <li>Vintage</li>
  <li>Long Exposure</li>
  <li>Horror</li>
  <li>Sunny</li>
  <li>Bright</li>
  <li>Hazy</li>
  <li>Bokeh</li>
  <li>Serene</li>
  <li>Texture</li>
  <li>Ethereal</li>
  <li>Macro</li>
  <li>Depth of Field</li>
  <li>Geometric Composition</li>
  <li>Minimal</li>
  <li>Romantic</li>
</ul>
