
namespace nPlan{
    class Plan{
    public:
        class Builder;  // Build all of Plan in one Step
        class Judge;    // Evaluate Plan based of patterns
        class Mason;    // Build Plan in a series of steps with trial and error
    };
}



namespace nSubspace{
    class Subspace{
        friend class nPlan::Plan;
        friend class nPlan::Plan::Builder;
        friend class nPlan::Plan::Judge;
        friend class nPlan::Plan::Mason;
    };
}

#include "File.CPP"