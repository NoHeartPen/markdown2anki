git filter-branch -f --env-filter "

OLD_EMAIL='NoHeartPen@outlook.com'
CORRECT_NAME='NoHeartPen'
CORRECT_EMAIL='19946710397@163.com'

if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
export GIT_COMMITTER_NAME="$CORRECT_NAME"
export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
export GIT_AUTHOR_NAME="$CORRECT_NAME"
export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
" --tag-name-filter cat -- --branches --tags
