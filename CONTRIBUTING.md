# Contributing In General
Our project welcomes external contributions. If you have an itch, please feel free to scratch it. 

To contribute code or documentation, please submit a [pull request](https://github.com/ibm/ibm_zos_zosmf/pulls). A good way to familiarize yourself with the codebase and contribution process is to look for and tackle low-hanging fruit in the [issue tracker](https://github.com/ibm/ibm_zos_zosmf/issues). Before embarking on a more ambitious contribution, please quickly [get in touch](#communication) with us.

**Note: We appreciate your effort, and want to avoid a situation where a contribution requires extensive rework (by you or by us), sits in backlog for a long time, or cannot be accepted at all!**


## Proposing new features
If you would like to implement a new feature, please [raise an issue](https://github.com/ibm/ibm_zos_zosmf/issues) before sending a pull request so the feature can be discussed. This is to avoid you wasting your valuable time working on a feature that the project developers
are not interested in accepting into the code base.


## Fixing bugs
If you would like to fix a bug, please [raise an issue](https://github.com/ibm/ibm_zos_zosmf/issues) before sending a pull request so it can be tracked.


## Merge approval
The project maintainers use LGTM (Looks Good To Me) in comments on the code review to indicate acceptance. A change requires LGTMs from two of the maintainers of each component affected. Please refer to [MAINTAINERS.md](MAINTAINERS.md) for a list of the maintainers
 
## Branch description
|Branch|Base|Description|
|------|----|-----------|
|master |	   |This is stable code that is [semantic](https://semver.org/) versioned that requires a pull request to merge into master.     |
|dev    |master|This is the development code that keeps developers in synch that has undegone a review and pull request that can be unstable.|
|feature|dev   |This is a temporary branch with feature code that is actively being developed thus unstable.                                 |
|release-vX.Y.Z|dev|This is a temporary release branch that following the [semantic](https://semver.org/) version that stabilized the release code, allowing for bugfix's to be made without the risk of feature code slipping into the release.|
|bugfix	|release-vX.Y.Z|This is a temporary branch with fixes for a release branch. The bugfix branch will be merged into the release branch and cherry-picked into the dev branch.|
|hotfix	|master|This is a temporary branch with a production code fix that should be merged into master and cherry-picked into dev and release branches.|

## Legal
Each source file must include a license header for [GPL License 3.0](https://opensource.org/licenses/GPL-3.0) or [Apache License 2.0](https://opensource.org/licenses/Apache-2.0):
```
# Copyright (c) IBM Corporation 2020 
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
```
```
# Copyright (c) IBM Corporation 2020 
# Apache License, Version 2.0 (see https://opensource.org/licenses/Apache-2.0)
```

We have tried to make it as easy as possible to make contributions. This applies to how we handle the legal aspects of contribution. We use the
same approach - the [Developer's Certificate of Origin 1.1 (DCO)](https://github.com/hyperledger/fabric/blob/master/docs/source/DCO1.1.txt) - that the Linux® Kernel [community](https://elinux.org/Developer_Certificate_Of_Origin) uses to manage code contributions.

We simply ask that when submitting a patch for review, the developer must include a sign-off statement in the commit message. Here is an example Signed-off-by line, which indicates that the submitter accepts the DCO:
```
Signed-off-by: John Doe <john.doe@example.com>
```

You can include this automatically when you commit a change to your local git repository using the following command:
```
git commit -s
```


## Communication
Please feel free to connect with us on our [Slack channel](https://app.slack.com/client/T1BAJVCTY/CGLJM7W4W).


## Setup
Please add any special setup instructions for your project to help the developer become productive quickly.


## Testing
Please provide information that helps the developer test any changes they make before submitting.


## Coding style guidelines
Optional, but recommended: please share any specific style guidelines you might have for your project.
