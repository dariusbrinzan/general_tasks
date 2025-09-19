Brinzan Darius Ionut


Challenge 1

    This script provides a simple utility function to retrieve a value from a nested dictionary using a /-separated key path.
    get_value(nested_dict, key_path) function: 
        -> Takes a nested Python dictionary and a string path such as "a/b/c".
        -> It iterates through each key in the path:

        -> Splits the path by /.

        -> Checks that the current level is a dictionary and contains the key.

        -> Updates the current reference until the final value is found.

        -> The function prints the traversal steps and raises a KeyError if any part of the path is    
           invalid.


Challenge 2

    I created a simulation of a pipeline in Azure DevOps. 
    
    From a writing perspective it was easier for me, and Azure DevOps uses the same YAML-based syntax as GitLab, so the overall patterns are pretty much the same.

    In the ci_cd_pipeline.png image I included an explanation for each stage, 
    along with notes on how to handle and manage the secrets and keys required to run the pipeline.

    The pipeline can also be enhanced by adding a CD stage triggered by ArgoCD.
     
    When the CI pipeline updates the Helm values file with the new image built during the CI process, ArgoCD is then triggered and deploys that newly created image.