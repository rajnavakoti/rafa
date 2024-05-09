# Contributing to RaFa

First off, thank you for considering contributing to RaFa. It's people like you that make RaFa such a great tool.

## Where do I go from here?

If you've noticed a bug or have a feature request, make one! It's generally best if you get confirmation of your bug or approval for your feature request this way before starting to code.

## Fork & create a branch

If this is something you think you can fix, then fork RaFa and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

```bash
git checkout -b 325-add-japanese-localisation
```

## Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first 😸

### Get the code

The first thing you'll need to do is get the code. The repository is at:

```bash
git clone https://github.com/yourusername/RaFa.git
```

### Test your changes

It's important to ensure your changes don't break anything.

### Create a pull request

At this point, you should switch back to your master branch and make sure it's up to date with RaFa's master branch:

```bash
git remote add upstream git@github.com:original/RaFa.git
git checkout master
git pull upstream master
```

Then update your feature branch from your local copy:

```bash
git checkout 325-add-japanese-localisation
git rebase master
git push --set-upstream origin 325-add-japanese-localisation
```
### Submitting a Pull Request

At this point, you're ready to make a pull request to the RaFa repository.

Navigate to the RaFa repository you just pushed to (e.g. https://github.com/yourusername/RaFa) and click the "Compare & pull request" button at the top of the repository.

GitHub will alert you that you're able to create a pull request in the main repository. Click the green "Create pull request" button.

### Keeping your Pull Request updated

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

To learn more about rebasing in Git, there are a lot of [good resources](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase) but here's the suggested workflow:

```bash
git checkout 325-add-japanese-localisation
git pull --rebase upstream master
git push --force-with-lease 325-add-japanese-localisation
```

### Merging a PR (maintainers only)

A PR can only be merged into master by a maintainer if:

It is passing CI.
It has been approved by at least two maintainers. If it was a maintainer who opened the PR, only one extra approval is needed.
It has no requested changes.
It is up to date with current master.

