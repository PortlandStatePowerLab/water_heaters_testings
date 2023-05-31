#ifndef MCP3008_H_
#define MCP3008_H_

class mcp3008{
	public:
		mcp3008(int channel);
		virtual ~mcp3008();
		float GetCurrent();

	private:
		int channel_;
};
#endif