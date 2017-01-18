
# Custom Authorizer

Lambda function for custom authorizer in API Gateway

![aws-services][aws-services-image]

## How To Setup a CodePipeline

- First, create a S3 Bucket where the deployment files will be uploaded with following below naming convention. *(You can use a different convention, but you need to add a permission for the CodeBuild to access this S3 bucket)*.

  >

      codepipeline-\<region\>-\<account_num\>-\<project_name\>

  like

      codepipeline-us-east-1-9999999999-aws-services-encryption


- Follow the steps in http://docs.aws.amazon.com/lambda/latest/dg/automating-deployment.html along with additional steps below.

  - When creating a new project in CodeBuild,

    > Under 'Advanced' setting, add an Environment variable , S3_BUCKET_NAME, with the S3 bucket name you created above.

  - When creating a build action whose mode is 'Create of replace a change set'

      - Set input parameter values of the SAM template and there are 2 ways to set the values

        1. Using a configuration file

          > Create a configuration json file that has input parameter values as below

                {
                    "Parameters": {
                      "SSOHost": "value1",
                      "SSOBasicAuthUsername": "value2",
                      "SSOBasicAuthPassword": "value2",
                      "SSOMasterToken": "value2"
                    }
                }

          > Set 'Template configuration' value using the name of the json file you created above following below format

              InputArtifactName::TemplateConfigurationFileName

          like

              MyAppBuild::env_dev.json

        2. Storing the values in the Setting

          > Set the parameter values in 'Parameter overrides' under 'Advanced' setting


## How To Test Lambda Functions

- $ cd tests
- Export environment variables, SSO_HOST, SSO_BASIC_AUTH_USERNAME, SSO_BASIC_AUTH_PASSWORD, SSO_MASTER_TOKEN
- Replace \<username\> and \<password\> with proper values in 'test_authorizer.py'
- $ python test_authorizer.py

[aws-services-image]: ./docs/images/logo.png?raw=true
