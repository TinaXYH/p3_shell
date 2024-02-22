# Automatic System Tests CI

## Trigger condition

```yaml
on: 
  push:
    tags:
      - test_*
```

## Detail steps to trigger actions

```bash
git push                        # push existing code to the remote repository
git tag test_featureA           # add tag "test_featureA" 
git push origin test_featureA   # push the tag to the remote repository
```

