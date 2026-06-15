class Solution {
public:
    set<pair<int, int>> visit = {};

    int dfs(vector<vector<int>>& grid, int i, int j) {
        if (i >= grid.size() or j >= grid[0].size() or i < 0 or j < 0 or grid[i][j] == 0)
            return 1;

        if (visit.count({i, j}))
            return 0;

        visit.insert({i, j});
        return (dfs(grid, i, j+1) + dfs(grid, i+1, j) + dfs(grid, i, j-1) + dfs(grid, i-1, j));
    }

    int islandPerimeter(vector<vector<int>>& grid) {
        for (int i = 0; i < grid.size(); i++)
            for (int j = 0; j < grid[0].size(); j++)
                if (grid[i][j] == 1)
                    return dfs(grid, i, j);
    }
};