### Playing with ReactJS

Playing with ReactJS the facebook framework for web UI. https://reactjs.org/docs/getting-started.html

#### Set the env.

To install node in your enviroment

```bash
@ECHO OFF
echo SETTING REACT JS DEV. ENVIRONMENT

SET REACT=D:\tools\node-v10.15.0-win-x64

SET PATH=%REACT%;%PATH%
```

#### Create a blank project and start it just to test
```bash
npx create-react-app my-app --template typescript
cd my-app
npm start
```


#### Autogenerate a rest client using OpenAPI contract
```bash
npm install @openapitools/openapi-generator-cli
npx openapi-generator-cli generate -i http://localhost:8080/v3/api-docs -g typescript-axios  -o ./generated-api-client
```
